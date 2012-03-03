import sys
import direct.directbase.DirectStart
from direct.directtools.DirectGeometry import LineNodePath

from direct.showbase.DirectObject import DirectObject
from direct.showbase.InputStateGlobal import inputState
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectButton import DirectButton

from panda3d.core import AmbientLight
from panda3d.core import DirectionalLight
from panda3d.core import Vec3
from panda3d.core import Vec4
from panda3d.core import Point3
from panda3d.core import TransformState
from panda3d.core import BitMask32

from panda3d.bullet import BulletWorld
from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletBoxShape
from panda3d.bullet import BulletSphereShape
from panda3d.bullet import BulletConeShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletDebugNode
from panda3d.bullet import ZUp

from Preloader import Preloader
import random

class LabTask03(DirectObject):
  
  #define the state of the game and level
  gameState = 'INIT'
  gameLevel = 1
  cameraState = 'STARTUP'
  count = 0
  attempts = 3
  posX = -200
  posY = 20
  posZ = 30
  score = 0
  contacts = 0
  pause = False
  fire = True
  desiredCamPos = Vec3(-200,30,20)

  def __init__(self):
    self.imageObject = OnscreenImage(image = 'models/splashscreen.png', pos=(0,0,0), scale=(1.4,1,1))
    preloader = Preloader()
    self.musicLoop = loader.loadSfx("music/loop/EndlessBliss.mp3")
    self.snowmansHit = loader.loadSfx("music/effects/snowball_hit.wav")
    self.candleThrow = loader.loadSfx("music/effects/snowball_throw.wav")
    self.presentHit = loader.loadSfx("music/effects/present_hit.wav")
    self.loseSound = loader.loadSfx("music/effects/Failure-WahWah.mp3")
    self.winSound = loader.loadSfx("music/effects/Ta Da-SoundBible.com-1884170640.mp3")
    self.nextLevelSound = loader.loadSfx("music/effects/button-17.wav")
    self.loseScreen = OnscreenImage(image = 'models/losescreen.png', pos=(0,0,0), scale=(1.4,1,1))
    self.loseScreen.hide()
    self.winScreen = OnscreenImage(image = 'models/winscreen.png', pos=(0,0,0), scale=(1.4,1,1))
    self.winScreen.hide()
    self.helpScreen = OnscreenImage(image = 'models/helpscreen.jpg', pos=(0,0,0.1), scale=(1,1,0.8))
    self.helpScreen.hide()
    self.backBtn = DirectButton(text=("Back"), scale = 0.1,  pos = (0,0,-0.8), command = self.doBack)
    self.retryBtn = DirectButton(text="Retry", scale = 0.1, pos = (0,0,0), command = self.doRetry)
    self.retryBtn.hide()
    self.menuBtn = DirectButton(text="Main Menu", scale = 0.1, pos = (0,0,0), command = self.doBack)
    self.menuBtn.hide()
    self.backBtn.hide()
    base.setBackgroundColor(0.1, 0.1, 0.8, 1)
    #base.setFrameRateMeter(True)
    
    # Position the camera
    base.cam.setPos(0, 30, 20)
    base.cam.lookAt(0, 30, 0)

    # Light
    alight = AmbientLight('ambientLight')
    alight.setColor(Vec4(0.5, 0.5, 0.5, 1))
    alightNP = render.attachNewNode(alight)

    dlight = DirectionalLight('directionalLight')
    dlight.setDirection(Vec3(1, 1, -1))
    dlight.setColor(Vec4(0.7, 0.7, 0.7, 1))
    dlightNP = render.attachNewNode(dlight)

    render.clearLight()
    render.setLight(alightNP)
    render.setLight(dlightNP)

    # Input
    self.accept('escape', self.doExit)
    self.accept('r', self.doReset)
    self.accept('f1', self.toggleWireframe)
    self.accept('f2', self.toggleTexture)
    self.accept('f3', self.toggleDebug)
    self.accept('f5', self.doScreenshot)
    self.accept('f', self.doShoot, [True])
    self.accept('p', self.doPause)

    inputState.watchWithModifiers('forward', 'w')
    inputState.watchWithModifiers('left', 'a')
    inputState.watchWithModifiers('reverse', 's')
    inputState.watchWithModifiers('right', 'd')
    inputState.watchWithModifiers('turnLeft', 'q')
    inputState.watchWithModifiers('turnRight', 'e')
    
    inputState.watchWithModifiers('moveLineUp', 'i')
    inputState.watchWithModifiers('moveLineDown','k')
    inputState.watchWithModifiers('moveLineRight','l')
    inputState.watchWithModifiers('moveLineLeft','j')
    
    self.font = loader.loadFont('models/SHOWG.TTF')
    self.font.setPixelsPerUnit(60)
    self.attemptText = OnscreenText(text='', pos = (0.9,0.8), scale = 0.07, font = self.font)
    self.levelText = OnscreenText(text='', pos=(-0.9,0.9), scale = 0.07, font = self.font )
    self.scoreText = OnscreenText(text='', pos = (0.9,0.9), scale = 0.07, font = self.font)
    self.text = OnscreenText(text = '', 
                              pos = (0, 0), scale = 0.07, font = self.font)
    self.pauseText = OnscreenText(text='P: Pause', pos= (0.9,0.7), scale = 0.05, font = self.font)
    self.pauseText.hide()
    # Task
    taskMgr.add(self.update, 'updateWorld')

    # Physics
    self.setup()

  # _____HANDLER_____
  
  def doRetry(self):
    self.loseScreen.hide()
    self.levelText.clearText()
    self.scoreText.clearText()
    self.attemptText.clearText()
    self.playGame()
    self.retryBtn.hide()
    self.cleanup()
    self.setup()
    

  def doExit(self):
    self.cleanup()
    sys.exit(1)

  def doReset(self):
    self.attempts = 3
    self.cameraState = 'STARTUP'
    base.cam.setPos(0,30,20)
    self.arrow.removeNode()
    self.scoreText.clearText()
    self.levelText.clearText()
    self.attemptText.clearText()
    self.cleanup()
    self.setup()
    
  def toggleWireframe(self):
    base.toggleWireframe()

  def toggleTexture(self):
    base.toggleTexture()

  def toggleDebug(self):
    if self.debugNP.isHidden():
      self.debugNP.show()
    else:
      self.debugNP.hide()

  def doScreenshot(self):
    base.screenshot('Bullet')
    
    
  def doShoot(self, ccd):
    if(self.fire and self.attempts > 0 and self.gameState == 'PLAY'):
      self.cameraState = 'LOOK'
      self.fire = False
      self.candleThrow.play()
      self.attempts -= 1
      #get from/to points from mouse click
      ## pMouse = base.mouseWatcherNode.getMouse()
      ## pFrom = Point3()
      ## pTo = Point3()
      ## base.camLens.extrude(pMouse, pFrom, pTo)
      
      ## pFrom = render.getRelativePoint(base.cam, pFrom)
      ## pTo = render.getRelativePoint(base.cam, pTo)
      
      # calculate initial velocity
      v = self.pTo - self.pFrom
      ratio = v.length() / 40
      v.normalize()
      v *= 70.0 * ratio
      torqueOffset = random.random() * 10
      
      #create bullet
      shape = BulletSphereShape(0.5)
      shape01 = BulletSphereShape(0.5)
      shape02 = BulletSphereShape(0.5)
      shape03 = BulletSphereShape(0.5)
      body = BulletRigidBodyNode('Candle')
      bodyNP = self.worldNP.attachNewNode(body)
      bodyNP.node().addShape(shape, TransformState.makePos(Point3(0,0,0)))
      bodyNP.node().addShape(shape01, TransformState.makePos(Point3(0,0.5,-0.5)))
      bodyNP.node().addShape(shape02,TransformState.makePos(Point3(0,1,-1)))
      bodyNP.node().addShape(shape03,TransformState.makePos(Point3(0,1.5,-1.5)))
      bodyNP.node().setMass(100)
      bodyNP.node().setFriction(1.0)
      bodyNP.node().setLinearVelocity(v)
      bodyNP.node().applyTorque(v*torqueOffset)
      bodyNP.setPos(self.pFrom)
      bodyNP.setCollideMask(BitMask32.allOn())
      
      visNP = loader.loadModel('models/projectile.X')
      visNP.setScale(0.7)
      visNP.clearModelNodes()
      visNP.reparentTo(bodyNP)
      
      #self.bird = bodyNP.node()
      
      if ccd:
          bodyNP.node().setCcdMotionThreshold(1e-7)
          bodyNP.node().setCcdSweptSphereRadius(0.5)
          
      self.world.attachRigidBody(bodyNP.node())
      
      #remove the bullet again after 1 sec
      self.bullets = bodyNP
      taskMgr.doMethodLater(5, self.removeBullet, 'removeBullet', extraArgs=[bodyNP], 
                            appendTask = True)
      
    
  def removeBullet(self, bulletNP, task):
    self.cameraState = 'STAY'
    self.fire = True
    self.world.removeRigidBody(bulletNP.node())
    bulletNP.removeNode()
    if(self.attempts <= 0 and len(self.snowmans)>0):
      self.gameState = 'LOSE'
      self.doContinue()
      
    return task.done

  # ____TASK___

  def processInput(self, dt):
    force = Vec3(0, 0, 0)
    torque = Vec3(0, 0, 0)
    #print self.pTo.getY()
    if inputState.isSet('forward'):
      if(self.pTo.getZ() < 40):
        self.pTo.addZ(0.5)
    if inputState.isSet('reverse'):
      if(self.pTo.getZ() > 0 ):
        self.pTo.addZ(-0.5)
    if inputState.isSet('left'):
      if(self.pTo.getY() < 100):
        self.pTo.addY(0.5)
        self.arrow.setScale(self.arrow.getSx(),self.arrow.getSy()-0.006,self.arrow.getSz())
    if inputState.isSet('right'):
      if(self.pTo.getY() > 60):
        self.pTo.addY(-0.5)
        self.arrow.setScale(self.arrow.getSx(),self.arrow.getSy()+0.006,self.arrow.getSz())
        
    self.arrow.lookAt(self.pTo)
    
  def processContacts(self, dt):
      for box in self.boxes:
        for snowman in self.snowmans:
          result = self.world.contactTestPair(box, snowman.node())
      
          if (result.getNumContacts() > 0):
            self.snowmansHit.play()
            self.score += 100
            self.text.setPos(0,0.7)
            self.text.setText("HIT")
            self.snowmans.remove(snowman)
            self.world.removeRigidBody(snowman.node())
            snowman.removeNode()
            if(len(self.snowmans)  <= 0):
              self.gameState = "NEXT"
              self.text.setText('Nice! Press space to continue')

              
      for box in self.boxes:
        for present in self.presents:
          result01 = self.world.contactTestPair(box,present.node())
          if(result01.getNumContacts() > 0):
            self.presents.remove(present)
            self.world.removeRigidBody(present.node())
            present.removeNode()
            self.presentHit.play()
            self.score += 500
            
  def doContinue(self):
    if(self.gameState == 'INIT'):
      self.gameState = 'MENU'
      self.text.clearText()
      self.musicLoop.setLoop(True)
      self.musicLoop.setVolume(0.5)
      self.musicLoop.play()
      self.startBtn = DirectButton(text=("Play"), scale = 0.1, pos = (0,0,0),command=self.playGame)
      self.helpBtn = DirectButton(text=("Help"), scale = 0.1, pos = (0,0,-0.2),command=self.help)
      self.exitBtn = DirectButton(text=("Exit"), scale = 0.1,  pos = (0,0,-0.4), command = self.doExit)
      return
    
    if self.gameState == 'NEXT':
      self.nextLevelSound.play()
      self.fire = True
      self.gameLevel += 1
      self.score += (self.attempts * 100)
      self.doReset()
      self.gameState = 'PLAY'
      return
    
    if self.gameState == 'LOSE':
      self.loseSound.play()
      self.arrow.removeNode()
      self.loseScreen.show()
      self.levelText.hide()
      self.attemptText.hide()
      self.scoreText.hide()
      self.text.hide()
      self.pauseText.hide()
      self.retryBtn.show()
      return
    
    if self.gameState == 'WIN':
      self.levelText.hide()
      self.attemptText.hide()
      self.scoreText.clearText()
      self.scoreText.setPos(0,0.6)
      self.scoreText.setText("%s"%self.score)
      self.winScreen.show()
      self.winSound.play()
      self.menuBtn.show()
      self.pauseText.hide()
      return
      
    
  def playGame(self):
    print "Play Game"
    self.attempts = 3
    self.score = 0
    self.gameLevel = 1
    self.gameState = 'PLAY'
    self.musicLoop.setVolume(0.3)
    self.imageObject.hide()
    self.startBtn.hide()
    self.exitBtn.hide()
    self.helpBtn.hide()
    self.cleanup()
    self.setup()
    
  def doBack(self):
    self.gameState = 'MENU'
    self.scoreText.setPos(0.9,0.9)
    self.scoreText.hide()
    self.imageObject.show()
    self.startBtn.show()
    self.exitBtn.show()
    self.helpBtn.show()
    self.helpScreen.hide()
    self.backBtn.hide()
    self.menuBtn.hide()
    self.winScreen.hide()
    
  def help(self):
    self.gameState = 'HELP'
    self.startBtn.hide()
    self.exitBtn.hide()
    self.helpBtn.hide()
    self.backBtn.show()
    self.helpScreen.show()
    return
    
  def doPause(self):
    self.pause  = not self.pause
    if(self.pause):
      self.text.setText("Pause")
    else:
      self.text.clearText()
      

  def update(self, task):

    dt = globalClock.getDt()
    if(not self.pause):
      if self.gameState == 'INIT':
        self.text.setPos(0,0)
        self.text.setText('Press space to continue')
        self.accept('space',self.doContinue)
          
      if self.gameState == 'PLAY':
        #print self.posZ
        #if(self.posX < -120):
        #  self.posX += 0.03
        #  self.posZ -= 0.02
        #elif(self.posZ < 70):
        #  self.posZ += 0.02;
        #elif(self.posZ > 70 and self.posX > -120):
        #  self.posZ -= 0.02
        #  self.posX -= 0.03
        #base.cam.setPos(self.posX, self.posZ, self.posY)
        self.levelText.setText('Level: %s'%self.gameLevel)
        self.attemptText.setText('Tries Left: %s'%self.attempts)
        self.scoreText.setText('Score: %s'%self.score)
        self.pauseText.show()
        self.processContacts(dt)
        self.world.doPhysics(dt, 20, 1.0/180.0)
        #self.drawLines()
        self.processInput(dt)
        
        if self.cameraState == 'STARTUP':
          oldPos = base.cam.getPos()
          pos = (oldPos*0.9) + (self.desiredCamPos*0.1)
          base.cam.setPos(pos)
          base.cam.lookAt(0,30,0)
        elif self.cameraState == 'STAY':
          #oldPos = base.cam.getPos()
          #currPos = (oldPos*0.9) + (self.desiredCamPos*0.1)
          #base.cam.setPos(currPos)
          base.cam.lookAt(0,30,0)
        elif self.cameraState == 'LOOK':
          base.cam.lookAt(self.bullets)
          #base.cam.setPos(-200,self.bullets.getZ(),20)
        
      if self.gameState == 'NEXT':
        self.world.doPhysics(dt, 20, 1.0/180.0)
        

      ## self.raycast()
    
    return task.cont
      
  def raycast(self):
    # Raycast for closest hit
    tsFrom = TransformState.makePos(Point3(0,0,0))
    tsTo = TransformState.makePos(Point3(10,0,0))
    shape = BulletSphereShape(0.5)
    penetration = 1.0
    result = self.world.sweepTestClosest(shape, tsFrom, tsTo, penetration)
    if result.hasHit():
        torque = Vec3(10,0,0)
        force = Vec3(0,0,100)
        
        ## for hit in result.getHits():
            ## hit.getNode().applyTorque(torque)
            ## hit.getNode().applyCentralForce(force)
        result.getNode().applyTorque(torque)
        result.getNode().applyCentralForce(force)
        ## print result.getClosestHitFraction()
        ## print result.getHitFraction(), \
            ## result.getNode(), \
            ## result.getHitPos(), \
            ## result.getHitNormal()

  def cleanup(self):
    self.world = None
    self.worldNP.removeNode()
    self.arrow.removeNode()
    self.lines.reset()
    self.text.clearText()

  def setup(self):
    self.attemptText.show()
    self.levelText.show()
    self.scoreText.show()
    self.text.show()
    
    self.worldNP = render.attachNewNode('World')

    # World
    self.debugNP = self.worldNP.attachNewNode(BulletDebugNode('Debug'))
    self.debugNP.show()

    self.world = BulletWorld()
    self.world.setGravity(Vec3(0, 0, -9.81))
    self.world.setDebugNode(self.debugNP.node())
    
    #arrow
    self.scaleY = 10
    self.arrow = loader.loadModel('models/arrow.X')
    self.arrow.setScale(0.5,0.5,0.5)
    self.arrow.setAlphaScale(0.5)
    #self.arrow.setTransparency(TransparencyAttrib.MAlpha) 
    self.arrow.reparentTo(render)
    
    #SkyBox
    skybox = loader.loadModel('models/skybox.X')
    skybox.reparentTo(render)

    # Ground
    shape = BulletPlaneShape(Vec3(0, 0, 1), 0)

    np = self.worldNP.attachNewNode(BulletRigidBodyNode('Ground'))
    np.node().addShape(shape)
    np.setPos(0, 0, -1)
    np.setCollideMask(BitMask32.allOn())

    self.world.attachRigidBody(np.node())
    
    visualNP = loader.loadModel('models/ground.X')
    visualNP.clearModelNodes()
    visualNP.reparentTo(np)
    
    #some boxes
    self.boxes = []
    self.snowmans = []
    self.platforms = []
    self.presents = []
    #TODO: Make a table
    #Table Top
    #self.createBox(Vec3(),Vec3())
    if(self.gameLevel == 1):
      self.createBox(Vec3(5,7,1),Vec3(0,5,10),1.0)
      #2 legs
      self.createBox(Vec3(4,1,4),Vec3(0,11,5),1.0)
      self.createBox(Vec3(4,1,4),Vec3(0,-1,5),1.0)
      
      # Pigs
      self.createSnowman(2.0,Vec3(0, 5, 2.0),10.0)
      self.createSnowman(1.5, Vec3(0,-10,4.0),10.0)
      
    if(self.gameLevel == 2):
      #table01
      self.createBox(Vec3(5,14,1),Vec3(0,-2,12),2.0)
      self.createBox(Vec3(5,7,1),Vec3(0,5,10),2.0)
      self.createBox(Vec3(4,1,4),Vec3(0,11,5),1.0)
      self.createBox(Vec3(4,1,4),Vec3(0,-1,5),1.0)
      #table02
      self.createBox(Vec3(5,7,1),Vec3(0,-9,10),2.0)
      self.createBox(Vec3(4,1,4),Vec3(0,-3,5),1.0)
      self.createBox(Vec3(4,1,4),Vec3(0,-15,5),1.0)
      #table03
      self.createBox(Vec3(1,1,1), Vec3(0,-1,14), 2.0)
      self.createBox(Vec3(1,1,1), Vec3(0,-3,14), 2.0)
      self.createBox(Vec3(1,1,1), Vec3(0,3,14), 2.0)
      self.createBox(Vec3(1,1,1), Vec3(0,-5,14), 2.0)
      self.createBox(Vec3(1,1,1), Vec3(0,5,14), 2.0)
      #pigs
      self.createSnowman(2.0,Vec3(0, 5, 2.0),10.0)
      self.createSnowman(2.0, Vec3(0,-9,2.0), 10.0)
      self.createSnowman(2.0,Vec3(0,-23,2.0),10.0)
      
    if(self.gameLevel == 3):
      #table01
      self.createBox(Vec3(4,2,2),Vec3(0,12,12),1.0)
      self.createBox(Vec3(4,1,4),Vec3(0,11,5),1.0)
      self.createBox(Vec3(4,1,4),Vec3(0,13,5),1.0)
      #table02
      self.createBox(Vec3(4,2,2),Vec3(0,-15,12),1.0)
      self.createBox(Vec3(4,1,4),Vec3(0,-14,5),1.0)
      self.createBox(Vec3(4,1,4),Vec3(0,-16,5),1.0)
      #table03
      self.createBox(Vec3(4,10,1),Vec3(0,-1,12),1.0)
      self.createBox(Vec3(4,10,1),Vec3(0,-1,14),1.0)
      self.createBox(Vec3(4,2,4),Vec3(0,-2,5),0.1)
      #table04
      self.createPlatform(Vec3(4,8,1),Vec3(0,7,16),1.0)
      self.createPlatform(Vec3(4,8,1),Vec3(0,-9,16),1.0)
      self.createBox(Vec3(4,1,3),Vec3(0,13,20),1.0)
      self.createBox(Vec3(4,1,3),Vec3(0,-16,20),1.0)
      #table05
      self.createBox(Vec3(4,15,1),Vec3(0,-1,24),1.0)
      self.createStoneBox(Vec3(1,1,1),Vec3(0,2,20),5.0)
      self.createStoneBox(Vec3(1,1,1),Vec3(0,-2,20),5.0)
      self.createStoneBox(Vec3(1,1,1),Vec3(0,4,20),5.0)
      self.createStoneBox(Vec3(1,1,1),Vec3(0,8,20),5.0)
      self.createStoneBox(Vec3(1,1,1),Vec3(0,6,20),5.0)
      
      #pigs
      self.createSnowman(2.0,Vec3(0, 5, 2.0),10.0)
      self.createSnowman(2.0,Vec3(0,-8.5,2.0),10.0)
      self.createSnowman(1.5, Vec3(0,-9,19.5), 7.0)
      
      #presents
      self.createPresent(Vec3(2,2,2),Vec3(0,-20,5))
         
    if(self.gameLevel == 4):
      #wall
      self.createStoneBox(Vec3(4,1.5,10), Vec3(0,20,10),20)
      #table01
      self.createBox(Vec3(4,1,5), Vec3(0,7,7),1)
      self.createBox(Vec3(4,1,5), Vec3(0,0,7),1)
      self.createBox(Vec3(4,1,4), Vec3(0,3,7),1)
      self.createPlatform(Vec3(5,8,1), Vec3(0,4,13),1)
      self.createBox(Vec3(4,1,3), Vec3(0,11,18),1)
      self.createBox(Vec3(4,1,3), Vec3(0,-3,18),1)
      self.createBox(Vec3(4,8,1), Vec3(0,4,25),1)
      self.createStoneBox(Vec3(1,1,1), Vec3(0,4,27),2)
      self.createStoneBox(Vec3(1,1,1), Vec3(0,7,27),2)
      self.createStoneBox(Vec3(1,1,1), Vec3(0,2,27),2)
      self.createStoneBox(Vec3(1,1,1), Vec3(0,2,29),2)
      #stairs
      self.createPlatform(Vec3(4,50,4), Vec3(0,-55,5),100)
      #table02
      self.createBox(Vec3(4,1,5), Vec3(0,-13,15),1)
      self.createBox(Vec3(4,1,5), Vec3(0,-20,15),1)
      self.createBox(Vec3(4,1,4), Vec3(0,-17,15),1)
      self.createPlatform(Vec3(4,8,1), Vec3(0,-16,22),1)
      self.createBox(Vec3(4,1,3), Vec3(0,-9,28),1)
      self.createBox(Vec3(4,1,3), Vec3(0,-23,28),1)
      self.createBox(Vec3(4,8,1), Vec3(0,-16,33),1)
      self.createStoneBox(Vec3(1,1,1), Vec3(0,-16,35),2)
      self.createStoneBox(Vec3(1,1,1), Vec3(0,-13,35),2)
      self.createStoneBox(Vec3(1,1,1), Vec3(0,-18,35),2)
      self.createStoneBox(Vec3(1,1,1), Vec3(0,-18,37),2)
      self.createStoneBox(Vec3(1,1,1), Vec3(0,-14,37),2)
      
      #snowman
      self.createSnowman(2.0,Vec3(0,30,5),1.0)
      self.createSnowman(1.5,Vec3(0,4,18),1.0)
      self.createSnowman(1.5,Vec3(0,-13,26),1.0)
      self.createSnowman(1.5,Vec3(0,-19,26),1.0)
      self.createSnowman(2.0,Vec3(0,12,5),1.0)
      self.createPresent(Vec3(2,2,2),Vec3(0,-25,13))
      self.createPresent(Vec3(3,3,3),Vec3(0,-30,13))
      self.createPresent(Vec3(4,4,4),Vec3(0,-36,13))
      #self.createSnowman(1.5,Vec3(0,4,20),1.0)

      
    if(self.gameLevel == 5):
      #table01
      self.createStoneBox(Vec3(4,7,3), Vec3(0,30,5),10.0)
      self.createStoneBox(Vec3(4,7,3), Vec3(0,-30,5),10.0)
      self.createBox(Vec3(4,1,3), Vec3(0,0,5), 1.0)
      self.createSnowman(1.5,Vec3(0,-6,5),1.0)
      self.createSnowman(1.5,Vec3(0,6,5),1.0)
      self.createBox(Vec3(4,1,3), Vec3(0,-12,5), 1.0)
      self.createBox(Vec3(4,1,3), Vec3(0,12,5), 1.0)
      self.createSnowman(1.5,Vec3(0,-18,5),1.0)
      self.createSnowman(1.5,Vec3(0,18,5),1.0)
      self.createStoneBox(Vec3(4,6,1),Vec3(0,-18,10), 0.1)
      self.createStoneBox(Vec3(4,6,1),Vec3(0,-6,10), 0.1)
      self.createStoneBox(Vec3(4,6,1),Vec3(0,6,10), 0.1)
      self.createStoneBox(Vec3(4,6,1),Vec3(0,18,10), 0.1)
      self.createStoneBox(Vec3(4,1,3),Vec3(0,23,14), 1.0)
      self.createStoneBox(Vec3(4,1,3),Vec3(0,-23,14), 1.0)
      self.createBox(Vec3(4,1,3),Vec3(0,18,14),1.0)
      self.createBox(Vec3(4,1,3),Vec3(0,-18,14),1.0)
      self.createStoneBox(Vec3(4,1,7),Vec3(0,13,20), 2.0)
      self.createStoneBox(Vec3(4,1,7),Vec3(0,-13,20), 2.0)
      self.createBox(Vec3(4,1,3),Vec3(0,8,14),1.0)
      self.createBox(Vec3(4,1,3),Vec3(0,-8,14),1.0)
      self.createStoneBox(Vec3(4,1,3),Vec3(0,3,14), 1.0)
      self.createStoneBox(Vec3(4,1,3),Vec3(0,-3,14), 1.0)
      self.createPlatform(Vec3(4,3.5,1),Vec3(0,-20 ,20), 1.0)
      self.createPlatform(Vec3(4,3.5,1),Vec3(0,20 ,20), 1.0)
      self.createPlatform(Vec3(4,3.5,1),Vec3(0,-5 ,20), 1.0)
      self.createPlatform(Vec3(4,3.5,1),Vec3(0,5 ,20), 1.0)
      self.createStoneBox(Vec3(4,1,3.5),Vec3(0,-18,25), 2.0)
      self.createStoneBox(Vec3(4,1,3.5),Vec3(0,18,25), 2.0)
      self.createStoneBox(Vec3(4,1,3.5),Vec3(0,-7.5,25), 2.0)
      self.createStoneBox(Vec3(4,1,3.5),Vec3(0,7.5,25), 2.0)
      self.createStoneBox(Vec3(4,6,1),Vec3(0,-12,30), 2.0)
      self.createStoneBox(Vec3(4,6,1),Vec3(0,12,30), 2.0)
      self.createBox(Vec3(4,1,5),Vec3(0,-5,30), 2.0)
      self.createBox(Vec3(4,1,5),Vec3(0,5,30), 2.0)
      self.createBox(Vec3(4,5,1),Vec3(0,0,40), 2.0)
      self.createPlatform(Vec3(4,2,0.5),Vec3(0,0,42), 2.0)
      self.createStoneBox(Vec3(4,0.5,2),Vec3(0,-3.5,45), 2.0)
      self.createStoneBox(Vec3(4,0.5,2),Vec3(0,3.5,45), 2.0)
      self.createStoneBox(Vec3(4,4,0.5),Vec3(0,0,48), 2.0)
      
      self.createPresent(Vec3(1.5,1.5,1.5),Vec3(0,22,30))
      self.createPresent(Vec3(1.5,1.5,1.5),Vec3(0,-22,30))
      self.createPresent(Vec3(2,2,1),Vec3(0,0,44))
      self.createPresent(Vec3(3,3,4),Vec3(0,0,33))
      
      
    if(self.gameLevel > 5):
      self.gameState = 'WIN'
      self.doContinue()
      return
        
    # drawing lines between the points 
    ## self.lines = LineNodePath(parent = render, thickness = 3.0, colorVec = Vec4(1, 0, 0, 1))
    ## self.pFrom = Point3(-4, 0, 0.5)
    ## self.pTo = Point3(4, 0, 0.5)
    
    # Aiming line 
    self.lines = LineNodePath(parent = render, thickness = 3.0, 
                              colorVec = Vec4(1, 0, 0, 1))
    self.pFrom = Point3(0, 100, 0.5)
    self.pTo = Point3(0, 60, 10)
    
    self.arrow.setPos(self.pFrom)
      
    
  def drawLines(self):  
    # Draws lines for the ray.
    self.lines.reset()  
    self.lines.drawLines([(self.pFrom,self.pTo)])
    self.lines.create()
    
  def createBox(self,size,pos,mass):
    shape = BulletBoxShape(size)
    body = BulletRigidBodyNode('Obstacle')
    bodyNP = self.worldNP.attachNewNode(body)
    bodyNP.node().addShape(shape)
    bodyNP.node().setMass(mass)
    bodyNP.node().setFriction(1.0)
    bodyNP.node().setDeactivationEnabled(False)
    bodyNP.setPos(pos)
    bodyNP.setCollideMask(BitMask32.allOn())

    self.world.attachRigidBody(bodyNP.node())
            
    visNP = loader.loadModel('models/crate.X')
    visNP.setScale(size*2)
    visNP.clearModelNodes()
    visNP.reparentTo(bodyNP)
    self.boxes.append(body)
    
  def createStoneBox(self,size,pos,mass):
    shape = BulletBoxShape(size)
    body = BulletRigidBodyNode('Obstacle')
    bodyNP = self.worldNP.attachNewNode(body)
    bodyNP.node().addShape(shape)
    bodyNP.node().setMass(mass)
    bodyNP.node().setFriction(1.0)
    bodyNP.node().setDeactivationEnabled(False)
    bodyNP.setPos(pos)
    bodyNP.setCollideMask(BitMask32.allOn())

    self.world.attachRigidBody(bodyNP.node())
            
    visNP = loader.loadModel('models/stone.X')
    visNP.setScale(size*2)
    visNP.clearModelNodes()
    visNP.reparentTo(bodyNP)
    self.boxes.append(body)
    
  def createSnowman(self, size, pos, mass):
    shape = BulletBoxShape(Vec3(size,size,size))
    shape01 = BulletSphereShape(size/2)
    body = BulletRigidBodyNode('Snowman')
    np = self.worldNP.attachNewNode(body)
    np.node().setMass(mass)
    np.node().addShape(shape, TransformState.makePos(Point3(0,0,-1)))
    np.node().addShape(shape01, TransformState.makePos(Point3(0,0,1)))
    np.node().setFriction(10.0)
    np.node().setDeactivationEnabled(False)
    np.setPos(pos)
    np.setCollideMask(BitMask32.allOn())
      
    self.world.attachRigidBody(np.node())
  
    visualNP = loader.loadModel('models/snowman.X')
    visualNP.setScale(size)
    visualNP.clearModelNodes()
    visualNP.reparentTo(np)
    self.snowmans.append(np)
    
  def createPlatform(self,size,pos,mass):
    shape = BulletBoxShape(size)
    body = BulletRigidBodyNode('Platform')
    bodyNP = self.worldNP.attachNewNode(body)
    bodyNP.node().addShape(shape)
    bodyNP.node().setMass(mass)
    bodyNP.node().setFriction(1.0)
    bodyNP.node().setDeactivationEnabled(False)
    bodyNP.setPos(pos)
    bodyNP.setCollideMask(BitMask32.allOn())

    self.world.attachRigidBody(bodyNP.node())
            
    visNP = loader.loadModel('models/crate.X')
    visNP.setScale(size*2)
    visNP.clearModelNodes()
    visNP.reparentTo(bodyNP)
    self.platforms.append(body)
    
  def createPresent(self,size,pos):
    shape = BulletBoxShape(size*0.7)
    body = BulletRigidBodyNode('Present')
    bodyNP = self.worldNP.attachNewNode(body)
    bodyNP.node().addShape(shape)
    bodyNP.node().setMass(1.0)
    bodyNP.node().setFriction(1.0)
    bodyNP.node().setDeactivationEnabled(False)
    bodyNP.setPos(pos)
    bodyNP.setCollideMask(BitMask32.allOn())
    
    self.world.attachRigidBody(bodyNP.node())
    
    visNP = loader.loadModel('models/present.X')
    visNP.setScale(size*2)
    visNP.clearModelNodes()
    visNP.reparentTo(bodyNP)
    self.presents.append(bodyNP)
    
    
game = LabTask03()
run()
