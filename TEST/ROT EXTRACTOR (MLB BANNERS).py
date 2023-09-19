import re

text = """
MLB - PLAYER TOTAL SINGLES
WILLIAM CONTRERAS - UNDER/OVER PLAYER SINGLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403003

OVER
7403004

UNDER
Sep 09 2:05 PM
Stream

OSWALD PERAZA - UNDER/OVER PLAYER SINGLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403005

OVER
7403006

UNDER
Sep 09 2:05 PM
Stream

KYLE HIGASHIOKA - UNDER/OVER PLAYER SINGLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403007

OVER
7403008

UNDER
Sep 09 2:05 PM
Stream

ANDRUW MONASTERIO - UNDER/OVER PLAYER SINGLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403009

OVER
7403010

UNDER
Sep 09 2:05 PM
Stream

CHRISTIAN YELICH - UNDER/OVER PLAYER SINGLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403011

OVER
7403012

UNDER
Sep 09 2:05 PM
Stream

TYRONE TAYLOR - UNDER/OVER PLAYER SINGLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403013

OVER
7403014

UNDER
Sep 09 2:05 PM
Stream

ANTHONY VOLPE - UNDER/OVER PLAYER SINGLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403015

OVER
7403016

UNDER
Sep 09 2:05 PM
Stream

DAVID JOHN LEMAHIEU - UNDER/OVER PLAYER SINGLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403017

OVER
7403018

UNDER
Sep 09 2:05 PM
Stream

GLEYBER TORRES - UNDER/OVER PLAYER SINGLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403019

OVER
7403020

UNDER
Sep 09 2:05 PM
Stream

GIANCARLO STANTON - UNDER/OVER PLAYER SINGLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403021

OVER
7403022

UNDER
Sep 09 2:05 PM
Stream

SAL FRELICK - UNDER/OVER PLAYER SINGLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403023

OVER
7403024

UNDER
Sep 09 2:05 PM
Stream

AARON JUDGE - UNDER/OVER PLAYER SINGLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403025

OVER
7403026

UNDER
Sep 09 2:05 PM
Stream

JASSON DOMINGUEZ - UNDER/OVER PLAYER SINGLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403027

OVER
7403028

UNDER
Sep 09 2:05 PM
Stream

BRICE TURANG - UNDER/OVER PLAYER SINGLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403029

OVER
7403030

UNDER
Sep 09 2:05 PM
Stream

WILLY ADAMES - UNDER/OVER PLAYER SINGLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403031

OVER
7403032

UNDER
Sep 09 2:05 PM
Stream

JORGE POLANCO - UNDER/OVER PLAYER SINGLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403033

OVER
7403034

UNDER
Sep 09 2:10 PM
Stream

WILLI CASTRO - UNDER/OVER PLAYER SINGLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403035

OVER
7403036

UNDER
Sep 09 2:10 PM
Stream

BRANDON NIMMO - UNDER/OVER PLAYER SINGLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403037

OVER
7403038

UNDER
Sep 09 2:10 PM
Stream

BRETT BATY - UNDER/OVER PLAYER SINGLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403039

OVER
7403040

UNDER
Sep 09 2:10 PM
Stream

KYLE FARMER - UNDER/OVER PLAYER SINGLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403041

OVER
7403042

UNDER
Sep 09 2:10 PM
Stream

OMAR NARVAEZ - UNDER/OVER PLAYER SINGLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403043

OVER
7403044

UNDER
Sep 09 2:10 PM
Stream

JEFF MCNEIL - UNDER/OVER PLAYER SINGLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403045

OVER
7403046

UNDER
Sep 09 2:10 PM
Stream

RAFAEL ORTEGA - UNDER/OVER PLAYER SINGLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403047

OVER
7403048

UNDER
Sep 09 2:10 PM
Stream

CARLOS CORREA - UNDER/OVER PLAYER SINGLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403049

OVER
7403050

UNDER
Sep 09 2:10 PM
Stream

JORDAN LUPLOW - UNDER/OVER PLAYER SINGLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403051

OVER
7403052

UNDER
Sep 09 2:10 PM
Stream

MARK VIENTOS - UNDER/OVER PLAYER SINGLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403053

OVER
7403054

UNDER
Sep 09 2:10 PM
Stream

RONNY MAURICIO - UNDER/OVER PLAYER SINGLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403055

OVER
7403056

UNDER
Sep 09 2:10 PM
Stream

MATT WALLNER - UNDER/OVER PLAYER SINGLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403057

OVER
7403058

UNDER
Sep 09 2:10 PM
Stream

RYAN JEFFERS - UNDER/OVER PLAYER SINGLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403059

OVER
7403060

UNDER
Sep 09 2:10 PM
Stream

ROYCE LEWIS - UNDER/OVER PLAYER SINGLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403061

OVER
7403062

UNDER
Sep 09 2:10 PM
Stream

FRANCISCO LINDOR - UNDER/OVER PLAYER SINGLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403063

OVER
7403064

UNDER
Sep 09 2:10 PM
Stream

DONOVAN SOLANO - UNDER/OVER PLAYER SINGLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403065

OVER
7403066

UNDER
Sep 09 2:10 PM
Stream

PETER ALONSO - UNDER/OVER PLAYER SINGLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403067

OVER
7403068

UNDER
Sep 09 2:10 PM
Stream

LOURDES GURRIEL - UNDER/OVER PLAYER SINGLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403069

OVER
7403070

UNDER
Sep 09 2:20 PM
Stream

EVAN LONGORIA - UNDER/OVER PLAYER SINGLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403071

OVER
7403072

UNDER
Sep 09 2:20 PM
Stream

EMMANUEL RIVERA - UNDER/OVER PLAYER SINGLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403073

OVER
7403074

UNDER
Sep 09 2:20 PM
Stream

CHRISTIAN WALKER - UNDER/OVER PLAYER SINGLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403075

OVER
7403076

UNDER
Sep 09 2:20 PM
Stream

TOMMY PHAM - UNDER/OVER PLAYER SINGLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403077

OVER
7403078

UNDER
Sep 09 2:20 PM
Stream

JEIMER CANDELARIO - UNDER/OVER PLAYER SINGLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403079

OVER
7403080

UNDER
Sep 09 2:20 PM
Stream

YAN GOMES - UNDER/OVER PLAYER SINGLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403081

OVER
7403082

UNDER
Sep 09 2:20 PM
Stream

CORBIN CARROLL - UNDER/OVER PLAYER SINGLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403083

OVER
7403084

UNDER
Sep 09 2:20 PM
Stream

IAN HAPP - UNDER/OVER PLAYER SINGLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403085

OVER
7403086

UNDER
Sep 09 2:20 PM
Stream

CODY BELLINGER - UNDER/OVER PLAYER SINGLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403087

OVER
7403088

UNDER
Sep 09 2:20 PM
Stream

MIKE TAUCHMAN - UNDER/OVER PLAYER SINGLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403089

OVER
7403090

UNDER
Sep 09 2:20 PM
Stream

NICK MADRIGAL - UNDER/OVER PLAYER SINGLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403091

OVER
7403092

UNDER
Sep 09 2:20 PM
Stream

GABRIEL MORENO - UNDER/OVER PLAYER SINGLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403093

OVER
7403094

UNDER
Sep 09 2:20 PM
Stream

DANSBY SWANSON - UNDER/OVER PLAYER SINGLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403095

OVER
7403096

UNDER
Sep 09 2:20 PM
Stream

NICO HOERNER - UNDER/OVER PLAYER SINGLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403097

OVER
7403098

UNDER
Sep 09 2:20 PM
Stream

KETEL MARTE - UNDER/OVER PLAYER SINGLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403099

OVER
7403100

UNDER
Sep 09 2:20 PM
Stream

SEIYA SUZUKI - UNDER/OVER PLAYER SINGLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403101

OVER
7403102

UNDER
Sep 09 2:20 PM
Stream

GERALDO PERDOMO - UNDER/OVER PLAYER SINGLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403103

OVER
7403104

UNDER
Sep 09 2:20 PM
Stream

JASON HEYWARD - UNDER/OVER PLAYER SINGLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403105

OVER
7403106

UNDER
Sep 09 4:05 PM
Stream

FREDDIE FREEMAN - UNDER/OVER PLAYER SINGLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403107

OVER
7403108

UNDER
Sep 09 4:05 PM
Stream

CARTER KIEBOOM - UNDER/OVER PLAYER SINGLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403109

OVER
7403110

UNDER
Sep 09 4:05 PM
Stream

MIGUEL ROJAS - UNDER/OVER PLAYER SINGLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403111

OVER
7403112

UNDER
Sep 09 4:05 PM
Stream

WILL SMITH - UNDER/OVER PLAYER SINGLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403113

OVER
7403114

UNDER
Sep 09 4:05 PM
Stream

ALEX CALL - UNDER/OVER PLAYER SINGLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403115

OVER
7403116

UNDER
Sep 09 4:05 PM
Stream

JAMES OUTMAN - UNDER/OVER PLAYER SINGLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403117

OVER
7403118

UNDER
Sep 09 4:05 PM
Stream

DOMINIC SMITH - UNDER/OVER PLAYER SINGLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403119

OVER
7403120

UNDER
Sep 09 4:05 PM
Stream

DAVID PERALTA - UNDER/OVER PLAYER SINGLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403121

OVER
7403122

UNDER
Sep 09 4:05 PM
Stream

KEIBERT RUIZ - UNDER/OVER PLAYER SINGLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403123

OVER
7403124

UNDER
Sep 09 4:05 PM
Stream

ENRIQUE HERNANDEZ - UNDER/OVER PLAYER SINGLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403125

OVER
7403126

UNDER
Sep 09 4:05 PM
Stream

JOEY MENESES - UNDER/OVER PLAYER SINGLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403127

OVER
7403128

UNDER
Sep 09 4:05 PM
Stream

LANE THOMAS - UNDER/OVER PLAYER SINGLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403129

OVER
7403130

UNDER
Sep 09 4:05 PM
Stream

JACOB YOUNG - UNDER/OVER PLAYER SINGLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403131

OVER
7403132

UNDER
Sep 09 4:05 PM
Stream

J.D. MARTINEZ - UNDER/OVER PLAYER SINGLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403133

OVER
7403134

UNDER
Sep 09 4:05 PM
Stream

CJ ABRAMS - UNDER/OVER PLAYER SINGLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403135

OVER
7403136

UNDER
Sep 09 4:05 PM
Stream

JAKE ALU - UNDER/OVER PLAYER SINGLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403137

OVER
7403138

UNDER
Sep 09 4:05 PM
Stream

MAX MUNCY - UNDER/OVER PLAYER SINGLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403139

OVER
7403140

UNDER
Sep 09 4:05 PM
Stream

EUGENIO SUAREZ - UNDER/OVER PLAYER SINGLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403141

OVER
7403142

UNDER
Sep 09 4:05 PM
Stream

TY FRANCE - UNDER/OVER PLAYER SINGLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403143

OVER
7403144

UNDER
Sep 09 4:05 PM
Stream

JOSH LOWE - UNDER/OVER PLAYER SINGLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403145

OVER
7403146

UNDER
Sep 09 4:05 PM
Stream

ISAAC PAREDES - UNDER/OVER PLAYER SINGLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403147

OVER
7403148

UNDER
Sep 09 4:05 PM
Stream

RANDY AROZARENA - UNDER/OVER PLAYER SINGLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403149

OVER
7403150

UNDER
Sep 09 4:05 PM
Stream

TAYLOR WALLS - UNDER/OVER PLAYER SINGLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403151

OVER
7403152

UNDER
Sep 09 4:05 PM
Stream

CHRISTIAN BETHANCOURT - UNDER/OVER PLAYER SINGLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403153

OVER
7403154

UNDER
Sep 09 4:05 PM
Stream

BRANDON LOWE - UNDER/OVER PLAYER SINGLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403155

OVER
7403156

UNDER
Sep 09 4:05 PM
Stream

TEOSCAR HERNÁNDEZ - UNDER/OVER PLAYER SINGLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403157

OVER
7403158

UNDER
Sep 09 4:05 PM
Stream

JOSHUA ROJAS - UNDER/OVER PLAYER SINGLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403159

OVER
7403160

UNDER
Sep 09 4:05 PM
Stream

DOMINIC CANZONE - UNDER/OVER PLAYER SINGLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403161

OVER
7403162

UNDER
Sep 09 4:05 PM
Stream

YANDY DIAZ - UNDER/OVER PLAYER SINGLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403163

OVER
7403164

UNDER
Sep 09 4:05 PM
Stream

J.P. CRAWFORD - UNDER/OVER PLAYER SINGLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403165

OVER
7403166

UNDER
Sep 09 4:05 PM
Stream

LUKE RALEY - UNDER/OVER PLAYER SINGLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403167

OVER
7403168

UNDER
Sep 09 4:05 PM
Stream

JULIO RODRIGUEZ - UNDER/OVER PLAYER SINGLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403169

OVER
7403170

UNDER
Sep 09 4:05 PM
Stream

MIKE FORD - UNDER/OVER PLAYER SINGLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403171

OVER
7403172

UNDER
Sep 09 4:05 PM
Stream

CAL RALEIGH - UNDER/OVER PLAYER SINGLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403173

OVER
7403174

UNDER
Sep 09 4:05 PM
Stream

JOSE SIRI - UNDER/OVER PLAYER SINGLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403175

OVER
7403176

UNDER
Sep 09 4:05 PM
Stream

ANTHONY SANTANDER - UNDER/OVER PLAYER SINGLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403177

OVER
7403178

UNDER
Sep 09 4:10 PM
Stream

RAMON URIAS - UNDER/OVER PLAYER SINGLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403179

OVER
7403180

UNDER
Sep 09 4:10 PM
Stream

JORGE MATEO - UNDER/OVER PLAYER SINGLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403181

OVER
7403182

UNDER
Sep 09 4:10 PM
Stream

RYAN MOUNTCASTLE - UNDER/OVER PLAYER SINGLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403183

OVER
7403184

UNDER
Sep 09 4:10 PM
Stream

AARON HICKS - UNDER/OVER PLAYER SINGLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403185

OVER
7403186

UNDER
Sep 09 4:10 PM
Stream

GUNNAR HENDERSON - UNDER/OVER PLAYER SINGLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403187

OVER
7403188

UNDER
Sep 09 4:10 PM
Stream

ALEX VERDUGO - UNDER/OVER PLAYER SINGLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403189

OVER
7403190

UNDER
Sep 09 4:10 PM
Stream

RAFAEL DEVERS - UNDER/OVER PLAYER SINGLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403191

OVER
7403192

UNDER
Sep 09 4:10 PM
Stream

TRISTON CASAS - UNDER/OVER PLAYER SINGLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403193

OVER
7403194

UNDER
Sep 09 4:10 PM
Stream

CONNOR WONG - UNDER/OVER PLAYER SINGLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403195

OVER
7403196

UNDER
Sep 09 4:10 PM
Stream

AUSTIN HAYS - UNDER/OVER PLAYER SINGLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403197

OVER
7403198

UNDER
Sep 09 4:10 PM
Stream

JAMES MCCANN - UNDER/OVER PLAYER SINGLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403199

OVER
7403200

UNDER
Sep 09 4:10 PM
Stream

ADAM DUVALL - UNDER/OVER PLAYER SINGLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403201

OVER
7403202

UNDER
Sep 09 4:10 PM
Stream

MASATAKA YOSHIDA - UNDER/OVER PLAYER SINGLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403203

OVER
7403204

UNDER
Sep 09 4:10 PM
Stream

JUSTIN TURNER - UNDER/OVER PLAYER SINGLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403205

OVER
7403206

UNDER
Sep 09 4:10 PM
Stream

ADLEY RUTSCHMAN - UNDER/OVER PLAYER SINGLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403207

OVER
7403208

UNDER
Sep 09 4:10 PM
Stream

TREVOR STORY - UNDER/OVER PLAYER SINGLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403209

OVER
7403210

UNDER
Sep 09 4:10 PM
Stream

KYLE SCHWARBER - UNDER/OVER PLAYER SINGLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403211

OVER
7403212

UNDER
Sep 09 6:05 PM
Stream

BRYCE HARPER - UNDER/OVER PLAYER SINGLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403213

OVER
7403214

UNDER
Sep 09 6:05 PM
Stream

BRYAN DE LA CRUZ - UNDER/OVER PLAYER SINGLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403215

OVER
7403216

UNDER
Sep 09 6:05 PM
Stream

JOSHUA EVAN BELL - UNDER/OVER PLAYER SINGLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403217

OVER
7403218

UNDER
Sep 09 6:05 PM
Stream

JAKE CAVE - UNDER/OVER PLAYER SINGLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403219

OVER
7403220

UNDER
Sep 09 6:05 PM
Stream

J.T. REALMUTO - UNDER/OVER PLAYER SINGLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403221

OVER
7403222

UNDER
Sep 09 6:05 PM
Stream

JOEY WENDLE - UNDER/OVER PLAYER SINGLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403223

OVER
7403224

UNDER
Sep 09 6:05 PM
Stream

BRANDON MARSH - UNDER/OVER PLAYER SINGLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403225

OVER
7403226

UNDER
Sep 09 6:05 PM
Stream

NICK FORTES - UNDER/OVER PLAYER SINGLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403227

OVER
7403228

UNDER
Sep 09 6:05 PM
Stream

BRYSON STOTT - UNDER/OVER PLAYER SINGLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403229

OVER
7403230

UNDER
Sep 09 6:05 PM
Stream

JACOB MICHAEL BURGER - UNDER/OVER PLAYER SINGLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403231

OVER
7403232

UNDER
Sep 09 6:05 PM
Stream

LUIS ARRAEZ - UNDER/OVER PLAYER SINGLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403233

OVER
7403234

UNDER
Sep 09 6:05 PM
Stream

ALEC BOHM - UNDER/OVER PLAYER SINGLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403235

OVER
7403236

UNDER
Sep 09 6:05 PM
Stream

NICK CASTELLANOS - UNDER/OVER PLAYER SINGLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403237

OVER
7403238

UNDER
Sep 09 6:05 PM
Stream

JESUS SANCHEZ - UNDER/OVER PLAYER SINGLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403239

OVER
7403240

UNDER
Sep 09 6:05 PM
Stream

TREA TURNER - UNDER/OVER PLAYER SINGLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403241

OVER
7403242

UNDER
Sep 09 6:05 PM
Stream

JAZZ CHISHOLM - UNDER/OVER PLAYER SINGLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403243

OVER
7403244

UNDER
Sep 09 6:05 PM
Stream

JORDAN WALKER - UNDER/OVER PLAYER SINGLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403245

OVER
7403246

UNDER
Sep 09 6:40 PM
Stream

LARS NOOTBAAR - UNDER/OVER PLAYER SINGLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403247

OVER
7403248

UNDER
Sep 09 6:40 PM
Stream

TYLER STEPHENSON - UNDER/OVER PLAYER SINGLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403249

OVER
7403250

UNDER
Sep 09 6:40 PM
Stream

TYLER O'NEILL - UNDER/OVER PLAYER SINGLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403251

OVER
7403252

UNDER
Sep 09 6:40 PM
Stream

PAUL GOLDSCHMIDT - UNDER/OVER PLAYER SINGLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403253

OVER
7403254

UNDER
Sep 09 6:40 PM
Stream

TOMMY EDMAN - UNDER/OVER PLAYER SINGLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403255

OVER
7403256

UNDER
Sep 09 6:40 PM
Stream

NICK SENZEL - UNDER/OVER PLAYER SINGLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403257

OVER
7403258

UNDER
Sep 09 6:40 PM
Stream

HARRISON BADER - UNDER/OVER PLAYER SINGLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403259

OVER
7403260

UNDER
Sep 09 6:40 PM
Stream

NOLAN GORMAN - UNDER/OVER PLAYER SINGLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403261

OVER
7403262

UNDER
Sep 09 6:40 PM
Stream

STUART FAIRCHILD - UNDER/OVER PLAYER SINGLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403263

OVER
7403264

UNDER
Sep 09 6:40 PM
Stream

WILLSON CONTRERAS - UNDER/OVER PLAYER SINGLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403265

OVER
7403266

UNDER
Sep 09 6:40 PM
Stream

MASYN WINN - UNDER/OVER PLAYER SINGLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403267

OVER
7403268

UNDER
Sep 09 6:40 PM
Stream

ELLY DE LA CRUZ - UNDER/OVER PLAYER SINGLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403269

OVER
7403270

UNDER
Sep 09 6:40 PM
Stream

NOLAN ARENADO - UNDER/OVER PLAYER SINGLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403271

OVER
7403272

UNDER
Sep 09 6:40 PM
Stream

SPENCER STEER - UNDER/OVER PLAYER SINGLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403273

OVER
7403274

UNDER
Sep 09 6:40 PM
Stream

HUNTER RENFROE - UNDER/OVER PLAYER SINGLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403275

OVER
7403276

UNDER
Sep 09 6:40 PM
Stream

CHRISTIAN ENCARNACION-STRAND - UNDER/OVER PLAYER SINGLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403277

OVER
7403278

UNDER
Sep 09 6:40 PM
Stream

NOELVI MARTE - UNDER/OVER PLAYER SINGLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403279

OVER
7403280

UNDER
Sep 09 6:40 PM
Stream

TRENT GRISHAM - UNDER/OVER PLAYER SINGLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403281

OVER
7403282

UNDER
Sep 09 7:10 PM
Stream

JOSE ALTUVE - UNDER/OVER PLAYER SINGLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403283

OVER
7403284

UNDER
Sep 09 7:10 PM
Stream

JEREMY PENA - UNDER/OVER PLAYER SINGLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403285

OVER
7403286

UNDER
Sep 09 7:10 PM
Stream

FERNANDO TATIS JR. - UNDER/OVER PLAYER SINGLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403287

OVER
7403288

UNDER
Sep 09 7:10 PM
Stream

XANDER BOGAERTS - UNDER/OVER PLAYER SINGLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403289

OVER
7403290

UNDER
Sep 09 7:10 PM
Stream

GARRETT COOPER - UNDER/OVER PLAYER SINGLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403291

OVER
7403292

UNDER
Sep 09 7:10 PM
Stream

MAURICIO DUBÓN - UNDER/OVER PLAYER SINGLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403293

OVER
7403294

UNDER
Sep 09 7:10 PM
Stream

YORDAN ALVAREZ - UNDER/OVER PLAYER SINGLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403295

OVER
7403296

UNDER
Sep 09 7:10 PM
Stream

JUAN SOTO - UNDER/OVER PLAYER SINGLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403297

OVER
7403298

UNDER
Sep 09 7:10 PM
Stream

MARTIN MALDONADO - UNDER/OVER PLAYER SINGLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403299

OVER
7403300

UNDER
Sep 09 7:10 PM
Stream

MANNY MACHADO - UNDER/OVER PLAYER SINGLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403301

OVER
7403302

UNDER
Sep 09 7:10 PM
Stream

MICHAEL BRANTLEY - UNDER/OVER PLAYER SINGLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403303

OVER
7403304

UNDER
Sep 09 7:10 PM
Stream

ALEX BREGMAN - UNDER/OVER PLAYER SINGLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403305

OVER
7403306

UNDER
Sep 09 7:10 PM
Stream

HA-SEONG KIM - UNDER/OVER PLAYER SINGLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403307

OVER
7403308

UNDER
Sep 09 7:10 PM
Stream

JOSE ABREU - UNDER/OVER PLAYER SINGLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403309

OVER
7403310

UNDER
Sep 09 7:10 PM
Stream

KYLE TUCKER - UNDER/OVER PLAYER SINGLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403311

OVER
7403312

UNDER
Sep 09 7:10 PM
Stream

LUIS CAMPUSANO - UNDER/OVER PLAYER SINGLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403313

OVER
7403314

UNDER
Sep 09 7:10 PM
Stream

RONALD ACUNA - UNDER/OVER PLAYER SINGLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403315

OVER
7403316

UNDER
Sep 09 7:20 PM
Stream

OZZIE ALBIES - UNDER/OVER PLAYER SINGLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403317

OVER
7403318

UNDER
Sep 09 7:20 PM
Stream

ALIKA WILLIAMS - UNDER/OVER PLAYER SINGLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403319

OVER
7403320

UNDER
Sep 09 7:20 PM
Stream

CONNOR JOE - UNDER/OVER PLAYER SINGLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403321

OVER
7403322

UNDER
Sep 09 7:20 PM
Stream

JI-HWAN BAE - UNDER/OVER PLAYER SINGLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403323

OVER
7403324

UNDER
Sep 09 7:20 PM
Stream

ENDY RODRIGUEZ - UNDER/OVER PLAYER SINGLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403325

OVER
7403326

UNDER
Sep 09 7:20 PM
Stream

ORLANDO ARCIA - UNDER/OVER PLAYER SINGLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403327

OVER
7403328

UNDER
Sep 09 7:20 PM
Stream

TRAVIS D'ARNAUD - UNDER/OVER PLAYER SINGLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403329

OVER
7403330

UNDER
Sep 09 7:20 PM
Stream

KE'BRYAN HAYES - UNDER/OVER PLAYER SINGLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403331

OVER
7403332

UNDER
Sep 09 7:20 PM
Stream

MARCELL OZUNA - UNDER/OVER PLAYER SINGLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403333

OVER
7403334

UNDER
Sep 09 7:20 PM
Stream

MICHAEL HARRIS - UNDER/OVER PLAYER SINGLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403335

OVER
7403336

UNDER
Sep 09 7:20 PM
Stream

MATT OLSON - UNDER/OVER PLAYER SINGLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403337

OVER
7403338

UNDER
Sep 09 7:20 PM
Stream

AUSTIN RILEY - UNDER/OVER PLAYER SINGLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403339

OVER
7403340

UNDER
Sep 09 7:20 PM
Stream

BRYAN REYNOLDS - UNDER/OVER PLAYER SINGLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403341

OVER
7403342

UNDER
Sep 09 7:20 PM
Stream

MIGUEL ANDÚJAR - UNDER/OVER PLAYER SINGLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403343

OVER
7403344

UNDER
Sep 09 7:20 PM
Stream

EDDIE ROSARIO - UNDER/OVER PLAYER SINGLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403345

OVER
7403346

UNDER
Sep 09 7:20 PM
Stream

JARED TRIOLO - UNDER/OVER PLAYER SINGLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403347

OVER
7403348

UNDER
Sep 09 7:20 PM
Stream

LIOVER PEGUERO - UNDER/OVER PLAYER SINGLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403349

OVER
7403350

UNDER
Sep 09 7:20 PM
Stream

JOC PEDERSON - UNDER/OVER PLAYER SINGLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403351

OVER
7403352

UNDER
Sep 09 9:05 PM
Stream

BRENDAN RODGERS - UNDER/OVER PLAYER SINGLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403353

OVER
7403354

UNDER
Sep 09 9:05 PM
Stream

LAMONTE WADE - UNDER/OVER PLAYER SINGLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403355

OVER
7403356

UNDER
Sep 09 9:05 PM
Stream

ELEHURIS MONTERO - UNDER/OVER PLAYER SINGLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403357

OVER
7403358

UNDER
Sep 09 9:05 PM
Stream

EZEQUIEL TOVAR - UNDER/OVER PLAYER SINGLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403359

OVER
7403360

UNDER
Sep 09 9:05 PM
Stream

CHARLIE BLACKMON - UNDER/OVER PLAYER SINGLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403361

OVER
7403362

UNDER
Sep 09 9:05 PM
Stream

BRANDON CRAWFORD - UNDER/OVER PLAYER SINGLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403363

OVER
7403364

UNDER
Sep 09 9:05 PM
Stream

JONATHAN GREGORY J D DAVIS - UNDER/OVER PLAYER SINGLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403365

OVER
7403366

UNDER
Sep 09 9:05 PM
Stream

MIKE YASTRZEMSKI - UNDER/OVER PLAYER SINGLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403367

OVER
7403368

UNDER
Sep 09 9:05 PM
Stream

BRENTON DOYLE - UNDER/OVER PLAYER SINGLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403369

OVER
7403370

UNDER
Sep 09 9:05 PM
Stream

WILMER FLORES - UNDER/OVER PLAYER SINGLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403371

OVER
7403372

UNDER
Sep 09 9:05 PM
Stream

RYAN MCMAHON - UNDER/OVER PLAYER SINGLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403373

OVER
7403374

UNDER
Sep 09 9:05 PM
Stream

MITCHELL HANIGER - UNDER/OVER PLAYER SINGLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403375

OVER
7403376

UNDER
Sep 09 9:05 PM
Stream

ELIAS DIAZ - UNDER/OVER PLAYER SINGLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403377

OVER
7403378

UNDER
Sep 09 9:05 PM
Stream

NOLAN JONES - UNDER/OVER PLAYER SINGLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403379

OVER
7403380

UNDER
Sep 09 9:05 PM
Stream

THAIRO ESTRADA - UNDER/OVER PLAYER SINGLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403381

OVER
7403382

UNDER
Sep 09 9:05 PM
Stream

BLAKE SABOL - UNDER/OVER PLAYER SINGLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403383

OVER
7403384

UNDER
Sep 09 9:05 PM
Stream

GABRIEL ARIAS - UNDER/OVER PLAYER SINGLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403385

OVER
7403386

UNDER
Sep 09 9:07 PM
Stream

ANDRES GIMENEZ - UNDER/OVER PLAYER SINGLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403387

OVER
7403388

UNDER
Sep 09 9:07 PM
Stream

KYREN PARIS - UNDER/OVER PLAYER SINGLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403389

OVER
7403390

UNDER
Sep 09 9:07 PM
Stream

RAMON LAUREANO - UNDER/OVER PLAYER SINGLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403391

OVER
7403392

UNDER
Sep 09 9:07 PM
Stream

JOSE RAMIREZ - UNDER/OVER PLAYER SINGLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403393

OVER
7403394

UNDER
Sep 09 9:07 PM
Stream

NOLAN SCHANUEL - UNDER/OVER PLAYER SINGLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403395

OVER
7403396

UNDER
Sep 09 9:07 PM
Stream

MYLES STRAW - UNDER/OVER PLAYER SINGLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403397

OVER
7403398

UNDER
Sep 09 9:07 PM
Stream

JOSH NAYLOR - UNDER/OVER PLAYER SINGLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403399

OVER
7403400

UNDER
Sep 09 9:07 PM
Stream

MIKE MOUSTAKAS - UNDER/OVER PLAYER SINGLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403401

OVER
7403402

UNDER
Sep 09 9:07 PM
Stream

BRANDON DRURY - UNDER/OVER PLAYER SINGLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403403

OVER
7403404

UNDER
Sep 09 9:07 PM
Stream

KOLE CALHOUN - UNDER/OVER PLAYER SINGLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403405

OVER
7403406

UNDER
Sep 09 9:07 PM
Stream

STEVEN KWAN - UNDER/OVER PLAYER SINGLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403407

OVER
7403408

UNDER
Sep 09 9:07 PM
Stream

RANDAL GRICHUK - UNDER/OVER PLAYER SINGLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403409

OVER
7403410

UNDER
Sep 09 9:07 PM
Stream

LOGAN O'HOPPE - UNDER/OVER PLAYER SINGLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403411

OVER
7403412

UNDER
Sep 09 9:07 PM
Stream

MJ MELENDEZ - UNDER/OVER PLAYER SINGLES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403413

OVER
7403414

UNDER
Sep 09 3:07 PM
Stream

MAIKEL GARCIA - UNDER/OVER PLAYER SINGLES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403415

OVER
7403416

UNDER
Sep 09 3:07 PM
Stream

MICHAEL MASSEY - UNDER/OVER PLAYER SINGLES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403417

OVER
7403418

UNDER
Sep 09 3:07 PM
Stream

BOBBY WITT JR. - UNDER/OVER PLAYER SINGLES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403419

OVER
7403420

UNDER
Sep 09 3:07 PM
Stream

SALVADOR PEREZ - UNDER/OVER PLAYER SINGLES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403421

OVER
7403422

UNDER
Sep 09 3:07 PM
Stream

DREW WATERS - UNDER/OVER PLAYER SINGLES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7403423

OVER
7403424

UNDER
Sep 09 3:07 PM
Stream

MLB - PLAYER TOTAL DOUBLES
BRICE TURANG - UNDER/OVER PLAYER DOUBLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404003

OVER
7404004

UNDER
Sep 09 2:05 PM
Stream

DAVID JOHN LEMAHIEU - UNDER/OVER PLAYER DOUBLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404005

OVER
7404006

UNDER
Sep 09 2:05 PM
Stream

JASSON DOMINGUEZ - UNDER/OVER PLAYER DOUBLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404007

OVER
7404008

UNDER
Sep 09 2:05 PM
Stream

OSWALD PERAZA - UNDER/OVER PLAYER DOUBLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404009

OVER
7404010

UNDER
Sep 09 2:05 PM
Stream

SAL FRELICK - UNDER/OVER PLAYER DOUBLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404011

OVER
7404012

UNDER
Sep 09 2:05 PM
Stream

WILLY ADAMES - UNDER/OVER PLAYER DOUBLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404013

OVER
7404014

UNDER
Sep 09 2:05 PM
Stream

GIANCARLO STANTON - UNDER/OVER PLAYER DOUBLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404015

OVER
7404016

UNDER
Sep 09 2:05 PM
Stream

ANDRUW MONASTERIO - UNDER/OVER PLAYER DOUBLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404017

OVER
7404018

UNDER
Sep 09 2:05 PM
Stream

ANTHONY VOLPE - UNDER/OVER PLAYER DOUBLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404019

OVER
7404020

UNDER
Sep 09 2:05 PM
Stream

AARON JUDGE - UNDER/OVER PLAYER DOUBLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404021

OVER
7404022

UNDER
Sep 09 2:05 PM
Stream

WILLIAM CONTRERAS - UNDER/OVER PLAYER DOUBLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404023

OVER
7404024

UNDER
Sep 09 2:05 PM
Stream

CHRISTIAN YELICH - UNDER/OVER PLAYER DOUBLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404025

OVER
7404026

UNDER
Sep 09 2:05 PM
Stream

KYLE HIGASHIOKA - UNDER/OVER PLAYER DOUBLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404027

OVER
7404028

UNDER
Sep 09 2:05 PM
Stream

TYRONE TAYLOR - UNDER/OVER PLAYER DOUBLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404029

OVER
7404030

UNDER
Sep 09 2:05 PM
Stream

GLEYBER TORRES - UNDER/OVER PLAYER DOUBLES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404031

OVER
7404032

UNDER
Sep 09 2:05 PM
Stream

BRETT BATY - UNDER/OVER PLAYER DOUBLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404033

OVER
7404034

UNDER
Sep 09 2:10 PM
Stream

JORGE POLANCO - UNDER/OVER PLAYER DOUBLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404035

OVER
7404036

UNDER
Sep 09 2:10 PM
Stream

WILLI CASTRO - UNDER/OVER PLAYER DOUBLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404037

OVER
7404038

UNDER
Sep 09 2:10 PM
Stream

RAFAEL ORTEGA - UNDER/OVER PLAYER DOUBLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404039

OVER
7404040

UNDER
Sep 09 2:10 PM
Stream

MATT WALLNER - UNDER/OVER PLAYER DOUBLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404041

OVER
7404042

UNDER
Sep 09 2:10 PM
Stream

JEFF MCNEIL - UNDER/OVER PLAYER DOUBLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404043

OVER
7404044

UNDER
Sep 09 2:10 PM
Stream

RONNY MAURICIO - UNDER/OVER PLAYER DOUBLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404045

OVER
7404046

UNDER
Sep 09 2:10 PM
Stream

BRANDON NIMMO - UNDER/OVER PLAYER DOUBLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404047

OVER
7404048

UNDER
Sep 09 2:10 PM
Stream

MARK VIENTOS - UNDER/OVER PLAYER DOUBLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404049

OVER
7404050

UNDER
Sep 09 2:10 PM
Stream

FRANCISCO LINDOR - UNDER/OVER PLAYER DOUBLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404051

OVER
7404052

UNDER
Sep 09 2:10 PM
Stream

JORDAN LUPLOW - UNDER/OVER PLAYER DOUBLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404053

OVER
7404054

UNDER
Sep 09 2:10 PM
Stream

PETER ALONSO - UNDER/OVER PLAYER DOUBLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404055

OVER
7404056

UNDER
Sep 09 2:10 PM
Stream

DONOVAN SOLANO - UNDER/OVER PLAYER DOUBLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404057

OVER
7404058

UNDER
Sep 09 2:10 PM
Stream

KYLE FARMER - UNDER/OVER PLAYER DOUBLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404059

OVER
7404060

UNDER
Sep 09 2:10 PM
Stream

OMAR NARVAEZ - UNDER/OVER PLAYER DOUBLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404061

OVER
7404062

UNDER
Sep 09 2:10 PM
Stream

RYAN JEFFERS - UNDER/OVER PLAYER DOUBLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404063

OVER
7404064

UNDER
Sep 09 2:10 PM
Stream

CARLOS CORREA - UNDER/OVER PLAYER DOUBLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404065

OVER
7404066

UNDER
Sep 09 2:10 PM
Stream

ROYCE LEWIS - UNDER/OVER PLAYER DOUBLES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404067

OVER
7404068

UNDER
Sep 09 2:10 PM
Stream

JEIMER CANDELARIO - UNDER/OVER PLAYER DOUBLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404069

OVER
7404070

UNDER
Sep 09 2:20 PM
Stream

CORBIN CARROLL - UNDER/OVER PLAYER DOUBLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404071

OVER
7404072

UNDER
Sep 09 2:20 PM
Stream

IAN HAPP - UNDER/OVER PLAYER DOUBLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404073

OVER
7404074

UNDER
Sep 09 2:20 PM
Stream

LOURDES GURRIEL - UNDER/OVER PLAYER DOUBLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404075

OVER
7404076

UNDER
Sep 09 2:20 PM
Stream

GABRIEL MORENO - UNDER/OVER PLAYER DOUBLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404077

OVER
7404078

UNDER
Sep 09 2:20 PM
Stream

TOMMY PHAM - UNDER/OVER PLAYER DOUBLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404079

OVER
7404080

UNDER
Sep 09 2:20 PM
Stream

YAN GOMES - UNDER/OVER PLAYER DOUBLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404081

OVER
7404082

UNDER
Sep 09 2:20 PM
Stream

CODY BELLINGER - UNDER/OVER PLAYER DOUBLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404083

OVER
7404084

UNDER
Sep 09 2:20 PM
Stream

MIKE TAUCHMAN - UNDER/OVER PLAYER DOUBLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404085

OVER
7404086

UNDER
Sep 09 2:20 PM
Stream

GERALDO PERDOMO - UNDER/OVER PLAYER DOUBLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404087

OVER
7404088

UNDER
Sep 09 2:20 PM
Stream

CHRISTIAN WALKER - UNDER/OVER PLAYER DOUBLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404089

OVER
7404090

UNDER
Sep 09 2:20 PM
Stream

EVAN LONGORIA - UNDER/OVER PLAYER DOUBLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404091

OVER
7404092

UNDER
Sep 09 2:20 PM
Stream

SEIYA SUZUKI - UNDER/OVER PLAYER DOUBLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404093

OVER
7404094

UNDER
Sep 09 2:20 PM
Stream

NICO HOERNER - UNDER/OVER PLAYER DOUBLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404095

OVER
7404096

UNDER
Sep 09 2:20 PM
Stream

EMMANUEL RIVERA - UNDER/OVER PLAYER DOUBLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404097

OVER
7404098

UNDER
Sep 09 2:20 PM
Stream

KETEL MARTE - UNDER/OVER PLAYER DOUBLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404099

OVER
7404100

UNDER
Sep 09 2:20 PM
Stream

DANSBY SWANSON - UNDER/OVER PLAYER DOUBLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404101

OVER
7404102

UNDER
Sep 09 2:20 PM
Stream

NICK MADRIGAL - UNDER/OVER PLAYER DOUBLES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404103

OVER
7404104

UNDER
Sep 09 2:20 PM
Stream

CJ ABRAMS - UNDER/OVER PLAYER DOUBLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404105

OVER
7404106

UNDER
Sep 09 4:05 PM
Stream

DAVID PERALTA - UNDER/OVER PLAYER DOUBLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404107

OVER
7404108

UNDER
Sep 09 4:05 PM
Stream

ENRIQUE HERNANDEZ - UNDER/OVER PLAYER DOUBLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404109

OVER
7404110

UNDER
Sep 09 4:05 PM
Stream

LANE THOMAS - UNDER/OVER PLAYER DOUBLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404111

OVER
7404112

UNDER
Sep 09 4:05 PM
Stream

JACOB YOUNG - UNDER/OVER PLAYER DOUBLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404113

OVER
7404114

UNDER
Sep 09 4:05 PM
Stream

J.D. MARTINEZ - UNDER/OVER PLAYER DOUBLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404115

OVER
7404116

UNDER
Sep 09 4:05 PM
Stream

ALEX CALL - UNDER/OVER PLAYER DOUBLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404117

OVER
7404118

UNDER
Sep 09 4:05 PM
Stream

MAX MUNCY - UNDER/OVER PLAYER DOUBLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404119

OVER
7404120

UNDER
Sep 09 4:05 PM
Stream

KEIBERT RUIZ - UNDER/OVER PLAYER DOUBLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404121

OVER
7404122

UNDER
Sep 09 4:05 PM
Stream

DOMINIC SMITH - UNDER/OVER PLAYER DOUBLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404123

OVER
7404124

UNDER
Sep 09 4:05 PM
Stream

JAMES OUTMAN - UNDER/OVER PLAYER DOUBLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404125

OVER
7404126

UNDER
Sep 09 4:05 PM
Stream

MIGUEL ROJAS - UNDER/OVER PLAYER DOUBLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404127

OVER
7404128

UNDER
Sep 09 4:05 PM
Stream

CARTER KIEBOOM - UNDER/OVER PLAYER DOUBLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404129

OVER
7404130

UNDER
Sep 09 4:05 PM
Stream

JAKE ALU - UNDER/OVER PLAYER DOUBLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404131

OVER
7404132

UNDER
Sep 09 4:05 PM
Stream

WILL SMITH - UNDER/OVER PLAYER DOUBLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404133

OVER
7404134

UNDER
Sep 09 4:05 PM
Stream

JASON HEYWARD - UNDER/OVER PLAYER DOUBLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404135

OVER
7404136

UNDER
Sep 09 4:05 PM
Stream

FREDDIE FREEMAN - UNDER/OVER PLAYER DOUBLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404137

OVER
7404138

UNDER
Sep 09 4:05 PM
Stream

JOEY MENESES - UNDER/OVER PLAYER DOUBLES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404139

OVER
7404140

UNDER
Sep 09 4:05 PM
Stream

ISAAC PAREDES - UNDER/OVER PLAYER DOUBLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404141

OVER
7404142

UNDER
Sep 09 4:05 PM
Stream

JULIO RODRIGUEZ - UNDER/OVER PLAYER DOUBLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404143

OVER
7404144

UNDER
Sep 09 4:05 PM
Stream

JOSHUA ROJAS - UNDER/OVER PLAYER DOUBLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404145

OVER
7404146

UNDER
Sep 09 4:05 PM
Stream

DOMINIC CANZONE - UNDER/OVER PLAYER DOUBLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404147

OVER
7404148

UNDER
Sep 09 4:05 PM
Stream

MIKE FORD - UNDER/OVER PLAYER DOUBLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404149

OVER
7404150

UNDER
Sep 09 4:05 PM
Stream

JOSH LOWE - UNDER/OVER PLAYER DOUBLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404151

OVER
7404152

UNDER
Sep 09 4:05 PM
Stream

BRANDON LOWE - UNDER/OVER PLAYER DOUBLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404153

OVER
7404154

UNDER
Sep 09 4:05 PM
Stream

EUGENIO SUAREZ - UNDER/OVER PLAYER DOUBLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404155

OVER
7404156

UNDER
Sep 09 4:05 PM
Stream

CHRISTIAN BETHANCOURT - UNDER/OVER PLAYER DOUBLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404157

OVER
7404158

UNDER
Sep 09 4:05 PM
Stream

LUKE RALEY - UNDER/OVER PLAYER DOUBLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404159

OVER
7404160

UNDER
Sep 09 4:05 PM
Stream

YANDY DIAZ - UNDER/OVER PLAYER DOUBLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404161

OVER
7404162

UNDER
Sep 09 4:05 PM
Stream

TEOSCAR HERNÁNDEZ - UNDER/OVER PLAYER DOUBLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404163

OVER
7404164

UNDER
Sep 09 4:05 PM
Stream

J.P. CRAWFORD - UNDER/OVER PLAYER DOUBLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404165

OVER
7404166

UNDER
Sep 09 4:05 PM
Stream

TAYLOR WALLS - UNDER/OVER PLAYER DOUBLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404167

OVER
7404168

UNDER
Sep 09 4:05 PM
Stream

RANDY AROZARENA - UNDER/OVER PLAYER DOUBLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404169

OVER
7404170

UNDER
Sep 09 4:05 PM
Stream

JOSE SIRI - UNDER/OVER PLAYER DOUBLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404171

OVER
7404172

UNDER
Sep 09 4:05 PM
Stream

CAL RALEIGH - UNDER/OVER PLAYER DOUBLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404173

OVER
7404174

UNDER
Sep 09 4:05 PM
Stream

TY FRANCE - UNDER/OVER PLAYER DOUBLES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404175

OVER
7404176

UNDER
Sep 09 4:05 PM
Stream

AUSTIN HAYS - UNDER/OVER PLAYER DOUBLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404177

OVER
7404178

UNDER
Sep 09 4:10 PM
Stream

JAMES MCCANN - UNDER/OVER PLAYER DOUBLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404179

OVER
7404180

UNDER
Sep 09 4:10 PM
Stream

RAMON URIAS - UNDER/OVER PLAYER DOUBLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404181

OVER
7404182

UNDER
Sep 09 4:10 PM
Stream

JUSTIN TURNER - UNDER/OVER PLAYER DOUBLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404183

OVER
7404184

UNDER
Sep 09 4:10 PM
Stream

ADAM DUVALL - UNDER/OVER PLAYER DOUBLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404185

OVER
7404186

UNDER
Sep 09 4:10 PM
Stream

ADLEY RUTSCHMAN - UNDER/OVER PLAYER DOUBLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404187

OVER
7404188

UNDER
Sep 09 4:10 PM
Stream

RYAN MOUNTCASTLE - UNDER/OVER PLAYER DOUBLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404189

OVER
7404190

UNDER
Sep 09 4:10 PM
Stream

TREVOR STORY - UNDER/OVER PLAYER DOUBLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404191

OVER
7404192

UNDER
Sep 09 4:10 PM
Stream

CONNOR WONG - UNDER/OVER PLAYER DOUBLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404193

OVER
7404194

UNDER
Sep 09 4:10 PM
Stream

RAFAEL DEVERS - UNDER/OVER PLAYER DOUBLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404195

OVER
7404196

UNDER
Sep 09 4:10 PM
Stream

ANTHONY SANTANDER - UNDER/OVER PLAYER DOUBLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404197

OVER
7404198

UNDER
Sep 09 4:10 PM
Stream

GUNNAR HENDERSON - UNDER/OVER PLAYER DOUBLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404199

OVER
7404200

UNDER
Sep 09 4:10 PM
Stream

AARON HICKS - UNDER/OVER PLAYER DOUBLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404201

OVER
7404202

UNDER
Sep 09 4:10 PM
Stream

TRISTON CASAS - UNDER/OVER PLAYER DOUBLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404203

OVER
7404204

UNDER
Sep 09 4:10 PM
Stream

JORGE MATEO - UNDER/OVER PLAYER DOUBLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404205

OVER
7404206

UNDER
Sep 09 4:10 PM
Stream

MASATAKA YOSHIDA - UNDER/OVER PLAYER DOUBLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404207

OVER
7404208

UNDER
Sep 09 4:10 PM
Stream

ALEX VERDUGO - UNDER/OVER PLAYER DOUBLES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404209

OVER
7404210

UNDER
Sep 09 4:10 PM
Stream

BRYAN DE LA CRUZ - UNDER/OVER PLAYER DOUBLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404211

OVER
7404212

UNDER
Sep 09 6:05 PM
Stream

ALEC BOHM - UNDER/OVER PLAYER DOUBLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404213

OVER
7404214

UNDER
Sep 09 6:05 PM
Stream

LUIS ARRAEZ - UNDER/OVER PLAYER DOUBLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404215

OVER
7404216

UNDER
Sep 09 6:05 PM
Stream

KYLE SCHWARBER - UNDER/OVER PLAYER DOUBLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404217

OVER
7404218

UNDER
Sep 09 6:05 PM
Stream

J.T. REALMUTO - UNDER/OVER PLAYER DOUBLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404219

OVER
7404220

UNDER
Sep 09 6:05 PM
Stream

BRANDON MARSH - UNDER/OVER PLAYER DOUBLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404221

OVER
7404222

UNDER
Sep 09 6:05 PM
Stream

JOSHUA EVAN BELL - UNDER/OVER PLAYER DOUBLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404223

OVER
7404224

UNDER
Sep 09 6:05 PM
Stream

TREA TURNER - UNDER/OVER PLAYER DOUBLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404225

OVER
7404226

UNDER
Sep 09 6:05 PM
Stream

BRYSON STOTT - UNDER/OVER PLAYER DOUBLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404227

OVER
7404228

UNDER
Sep 09 6:05 PM
Stream

JESUS SANCHEZ - UNDER/OVER PLAYER DOUBLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404229

OVER
7404230

UNDER
Sep 09 6:05 PM
Stream

NICK CASTELLANOS - UNDER/OVER PLAYER DOUBLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404231

OVER
7404232

UNDER
Sep 09 6:05 PM
Stream

JACOB MICHAEL BURGER - UNDER/OVER PLAYER DOUBLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404233

OVER
7404234

UNDER
Sep 09 6:05 PM
Stream

JAKE CAVE - UNDER/OVER PLAYER DOUBLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404235

OVER
7404236

UNDER
Sep 09 6:05 PM
Stream

NICK FORTES - UNDER/OVER PLAYER DOUBLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404237

OVER
7404238

UNDER
Sep 09 6:05 PM
Stream

JAZZ CHISHOLM - UNDER/OVER PLAYER DOUBLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404239

OVER
7404240

UNDER
Sep 09 6:05 PM
Stream

BRYCE HARPER - UNDER/OVER PLAYER DOUBLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404241

OVER
7404242

UNDER
Sep 09 6:05 PM
Stream

JOEY WENDLE - UNDER/OVER PLAYER DOUBLES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404243

OVER
7404244

UNDER
Sep 09 6:05 PM
Stream

STUART FAIRCHILD - UNDER/OVER PLAYER DOUBLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404245

OVER
7404246

UNDER
Sep 09 6:40 PM
Stream

NOLAN ARENADO - UNDER/OVER PLAYER DOUBLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404247

OVER
7404248

UNDER
Sep 09 6:40 PM
Stream

TYLER O'NEILL - UNDER/OVER PLAYER DOUBLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404249

OVER
7404250

UNDER
Sep 09 6:40 PM
Stream

HARRISON BADER - UNDER/OVER PLAYER DOUBLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404251

OVER
7404252

UNDER
Sep 09 6:40 PM
Stream

NOLAN GORMAN - UNDER/OVER PLAYER DOUBLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404253

OVER
7404254

UNDER
Sep 09 6:40 PM
Stream

SPENCER STEER - UNDER/OVER PLAYER DOUBLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404255

OVER
7404256

UNDER
Sep 09 6:40 PM
Stream

NOELVI MARTE - UNDER/OVER PLAYER DOUBLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404257

OVER
7404258

UNDER
Sep 09 6:40 PM
Stream

MASYN WINN - UNDER/OVER PLAYER DOUBLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404259

OVER
7404260

UNDER
Sep 09 6:40 PM
Stream

WILLSON CONTRERAS - UNDER/OVER PLAYER DOUBLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404261

OVER
7404262

UNDER
Sep 09 6:40 PM
Stream

TOMMY EDMAN - UNDER/OVER PLAYER DOUBLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404263

OVER
7404264

UNDER
Sep 09 6:40 PM
Stream

HUNTER RENFROE - UNDER/OVER PLAYER DOUBLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404265

OVER
7404266

UNDER
Sep 09 6:40 PM
Stream

LARS NOOTBAAR - UNDER/OVER PLAYER DOUBLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404267

OVER
7404268

UNDER
Sep 09 6:40 PM
Stream

CHRISTIAN ENCARNACION-STRAND - UNDER/OVER PLAYER DOUBLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404269

OVER
7404270

UNDER
Sep 09 6:40 PM
Stream

ELLY DE LA CRUZ - UNDER/OVER PLAYER DOUBLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404271

OVER
7404272

UNDER
Sep 09 6:40 PM
Stream

PAUL GOLDSCHMIDT - UNDER/OVER PLAYER DOUBLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404273

OVER
7404274

UNDER
Sep 09 6:40 PM
Stream

NICK SENZEL - UNDER/OVER PLAYER DOUBLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404275

OVER
7404276

UNDER
Sep 09 6:40 PM
Stream

JORDAN WALKER - UNDER/OVER PLAYER DOUBLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404277

OVER
7404278

UNDER
Sep 09 6:40 PM
Stream

TYLER STEPHENSON - UNDER/OVER PLAYER DOUBLES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404279

OVER
7404280

UNDER
Sep 09 6:40 PM
Stream

MAURICIO DUBÓN - UNDER/OVER PLAYER DOUBLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404281

OVER
7404282

UNDER
Sep 09 7:10 PM
Stream

MICHAEL BRANTLEY - UNDER/OVER PLAYER DOUBLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404283

OVER
7404284

UNDER
Sep 09 7:10 PM
Stream

LUIS CAMPUSANO - UNDER/OVER PLAYER DOUBLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404285

OVER
7404286

UNDER
Sep 09 7:10 PM
Stream

JOSE ABREU - UNDER/OVER PLAYER DOUBLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404287

OVER
7404288

UNDER
Sep 09 7:10 PM
Stream

KYLE TUCKER - UNDER/OVER PLAYER DOUBLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404289

OVER
7404290

UNDER
Sep 09 7:10 PM
Stream

TRENT GRISHAM - UNDER/OVER PLAYER DOUBLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404291

OVER
7404292

UNDER
Sep 09 7:10 PM
Stream

HA-SEONG KIM - UNDER/OVER PLAYER DOUBLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404293

OVER
7404294

UNDER
Sep 09 7:10 PM
Stream

JEREMY PENA - UNDER/OVER PLAYER DOUBLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404295

OVER
7404296

UNDER
Sep 09 7:10 PM
Stream

YORDAN ALVAREZ - UNDER/OVER PLAYER DOUBLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404297

OVER
7404298

UNDER
Sep 09 7:10 PM
Stream

MARTIN MALDONADO - UNDER/OVER PLAYER DOUBLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404299

OVER
7404300

UNDER
Sep 09 7:10 PM
Stream

XANDER BOGAERTS - UNDER/OVER PLAYER DOUBLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404301

OVER
7404302

UNDER
Sep 09 7:10 PM
Stream

GARRETT COOPER - UNDER/OVER PLAYER DOUBLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404303

OVER
7404304

UNDER
Sep 09 7:10 PM
Stream

MANNY MACHADO - UNDER/OVER PLAYER DOUBLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404305

OVER
7404306

UNDER
Sep 09 7:10 PM
Stream

ALEX BREGMAN - UNDER/OVER PLAYER DOUBLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404307

OVER
7404308

UNDER
Sep 09 7:10 PM
Stream

FERNANDO TATIS JR. - UNDER/OVER PLAYER DOUBLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404309

OVER
7404310

UNDER
Sep 09 7:10 PM
Stream

JOSE ALTUVE - UNDER/OVER PLAYER DOUBLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404311

OVER
7404312

UNDER
Sep 09 7:10 PM
Stream

JUAN SOTO - UNDER/OVER PLAYER DOUBLES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404313

OVER
7404314

UNDER
Sep 09 7:10 PM
Stream

ENDY RODRIGUEZ - UNDER/OVER PLAYER DOUBLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404315

OVER
7404316

UNDER
Sep 09 7:20 PM
Stream

JI-HWAN BAE - UNDER/OVER PLAYER DOUBLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404317

OVER
7404318

UNDER
Sep 09 7:20 PM
Stream

AUSTIN RILEY - UNDER/OVER PLAYER DOUBLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404319

OVER
7404320

UNDER
Sep 09 7:20 PM
Stream

KE'BRYAN HAYES - UNDER/OVER PLAYER DOUBLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404321

OVER
7404322

UNDER
Sep 09 7:20 PM
Stream

MATT OLSON - UNDER/OVER PLAYER DOUBLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404323

OVER
7404324

UNDER
Sep 09 7:20 PM
Stream

MICHAEL HARRIS - UNDER/OVER PLAYER DOUBLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404325

OVER
7404326

UNDER
Sep 09 7:20 PM
Stream

TRAVIS D'ARNAUD - UNDER/OVER PLAYER DOUBLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404327

OVER
7404328

UNDER
Sep 09 7:20 PM
Stream

LIOVER PEGUERO - UNDER/OVER PLAYER DOUBLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404329

OVER
7404330

UNDER
Sep 09 7:20 PM
Stream

MIGUEL ANDÚJAR - UNDER/OVER PLAYER DOUBLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404331

OVER
7404332

UNDER
Sep 09 7:20 PM
Stream

JARED TRIOLO - UNDER/OVER PLAYER DOUBLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404333

OVER
7404334

UNDER
Sep 09 7:20 PM
Stream

MARCELL OZUNA - UNDER/OVER PLAYER DOUBLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404335

OVER
7404336

UNDER
Sep 09 7:20 PM
Stream

OZZIE ALBIES - UNDER/OVER PLAYER DOUBLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404337

OVER
7404338

UNDER
Sep 09 7:20 PM
Stream

ORLANDO ARCIA - UNDER/OVER PLAYER DOUBLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404339

OVER
7404340

UNDER
Sep 09 7:20 PM
Stream

ALIKA WILLIAMS - UNDER/OVER PLAYER DOUBLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404341

OVER
7404342

UNDER
Sep 09 7:20 PM
Stream

CONNOR JOE - UNDER/OVER PLAYER DOUBLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404343

OVER
7404344

UNDER
Sep 09 7:20 PM
Stream

EDDIE ROSARIO - UNDER/OVER PLAYER DOUBLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404345

OVER
7404346

UNDER
Sep 09 7:20 PM
Stream

RONALD ACUNA - UNDER/OVER PLAYER DOUBLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404347

OVER
7404348

UNDER
Sep 09 7:20 PM
Stream

BRYAN REYNOLDS - UNDER/OVER PLAYER DOUBLES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404349

OVER
7404350

UNDER
Sep 09 7:20 PM
Stream

MIKE YASTRZEMSKI - UNDER/OVER PLAYER DOUBLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404351

OVER
7404352

UNDER
Sep 09 9:05 PM
Stream

CHARLIE BLACKMON - UNDER/OVER PLAYER DOUBLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404353

OVER
7404354

UNDER
Sep 09 9:05 PM
Stream

JONATHAN GREGORY J D DAVIS - UNDER/OVER PLAYER DOUBLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404355

OVER
7404356

UNDER
Sep 09 9:05 PM
Stream

BRENTON DOYLE - UNDER/OVER PLAYER DOUBLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404357

OVER
7404358

UNDER
Sep 09 9:05 PM
Stream

THAIRO ESTRADA - UNDER/OVER PLAYER DOUBLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404359

OVER
7404360

UNDER
Sep 09 9:05 PM
Stream

RYAN MCMAHON - UNDER/OVER PLAYER DOUBLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404361

OVER
7404362

UNDER
Sep 09 9:05 PM
Stream

JOC PEDERSON - UNDER/OVER PLAYER DOUBLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404363

OVER
7404364

UNDER
Sep 09 9:05 PM
Stream

BRANDON CRAWFORD - UNDER/OVER PLAYER DOUBLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404365

OVER
7404366

UNDER
Sep 09 9:05 PM
Stream

ELEHURIS MONTERO - UNDER/OVER PLAYER DOUBLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404367

OVER
7404368

UNDER
Sep 09 9:05 PM
Stream

NOLAN JONES - UNDER/OVER PLAYER DOUBLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404369

OVER
7404370

UNDER
Sep 09 9:05 PM
Stream

BLAKE SABOL - UNDER/OVER PLAYER DOUBLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404371

OVER
7404372

UNDER
Sep 09 9:05 PM
Stream

LAMONTE WADE - UNDER/OVER PLAYER DOUBLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404373

OVER
7404374

UNDER
Sep 09 9:05 PM
Stream

MITCHELL HANIGER - UNDER/OVER PLAYER DOUBLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404375

OVER
7404376

UNDER
Sep 09 9:05 PM
Stream

EZEQUIEL TOVAR - UNDER/OVER PLAYER DOUBLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404377

OVER
7404378

UNDER
Sep 09 9:05 PM
Stream

ELIAS DIAZ - UNDER/OVER PLAYER DOUBLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404379

OVER
7404380

UNDER
Sep 09 9:05 PM
Stream

BRENDAN RODGERS - UNDER/OVER PLAYER DOUBLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404381

OVER
7404382

UNDER
Sep 09 9:05 PM
Stream

WILMER FLORES - UNDER/OVER PLAYER DOUBLES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404383

OVER
7404384

UNDER
Sep 09 9:05 PM
Stream

JOSH NAYLOR - UNDER/OVER PLAYER DOUBLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404385

OVER
7404386

UNDER
Sep 09 9:07 PM
Stream

NOLAN SCHANUEL - UNDER/OVER PLAYER DOUBLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404387

OVER
7404388

UNDER
Sep 09 9:07 PM
Stream

RAMON LAUREANO - UNDER/OVER PLAYER DOUBLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404389

OVER
7404390

UNDER
Sep 09 9:07 PM
Stream

ANDRES GIMENEZ - UNDER/OVER PLAYER DOUBLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404391

OVER
7404392

UNDER
Sep 09 9:07 PM
Stream

STEVEN KWAN - UNDER/OVER PLAYER DOUBLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404393

OVER
7404394

UNDER
Sep 09 9:07 PM
Stream

RANDAL GRICHUK - UNDER/OVER PLAYER DOUBLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404395

OVER
7404396

UNDER
Sep 09 9:07 PM
Stream

MYLES STRAW - UNDER/OVER PLAYER DOUBLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404397

OVER
7404398

UNDER
Sep 09 9:07 PM
Stream

LOGAN O'HOPPE - UNDER/OVER PLAYER DOUBLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404399

OVER
7404400

UNDER
Sep 09 9:07 PM
Stream

KYREN PARIS - UNDER/OVER PLAYER DOUBLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404401

OVER
7404402

UNDER
Sep 09 9:07 PM
Stream

JOSE RAMIREZ - UNDER/OVER PLAYER DOUBLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404403

OVER
7404404

UNDER
Sep 09 9:07 PM
Stream

KOLE CALHOUN - UNDER/OVER PLAYER DOUBLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404405

OVER
7404406

UNDER
Sep 09 9:07 PM
Stream

MIKE MOUSTAKAS - UNDER/OVER PLAYER DOUBLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404407

OVER
7404408

UNDER
Sep 09 9:07 PM
Stream

GABRIEL ARIAS - UNDER/OVER PLAYER DOUBLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404409

OVER
7404410

UNDER
Sep 09 9:07 PM
Stream

BRANDON DRURY - UNDER/OVER PLAYER DOUBLES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404411

OVER
7404412

UNDER
Sep 09 9:07 PM
Stream

SALVADOR PEREZ - UNDER/OVER PLAYER DOUBLES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404413

OVER
7404414

UNDER
Sep 09 3:07 PM
Stream

MICHAEL MASSEY - UNDER/OVER PLAYER DOUBLES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404415

OVER
7404416

UNDER
Sep 09 3:07 PM
Stream

DREW WATERS - UNDER/OVER PLAYER DOUBLES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404417

OVER
7404418

UNDER
Sep 09 3:07 PM
Stream

MJ MELENDEZ - UNDER/OVER PLAYER DOUBLES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404419

OVER
7404420

UNDER
Sep 09 3:07 PM
Stream

BOBBY WITT JR. - UNDER/OVER PLAYER DOUBLES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404421

OVER
7404422

UNDER
Sep 09 3:07 PM
Stream

MAIKEL GARCIA - UNDER/OVER PLAYER DOUBLES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7404423

OVER
7404424

UNDER
Sep 09 3:07 PM
Stream

MLB - PLAYER TOTAL STOLEN BASES
ANDRUW MONASTERIO - UNDER/OVER PLAYER STOLEN BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405003

OVER
7405004

UNDER
Sep 09 2:05 PM
Stream

ANTHONY VOLPE - UNDER/OVER PLAYER STOLEN BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405005

OVER
7405006

UNDER
Sep 09 2:05 PM
Stream

DAVID JOHN LEMAHIEU - UNDER/OVER PLAYER STOLEN BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405007

OVER
7405008

UNDER
Sep 09 2:05 PM
Stream

BRICE TURANG - UNDER/OVER PLAYER STOLEN BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405009

OVER
7405010

UNDER
Sep 09 2:05 PM
Stream

WILLY ADAMES - UNDER/OVER PLAYER STOLEN BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405011

OVER
7405012

UNDER
Sep 09 2:05 PM
Stream

SAL FRELICK - UNDER/OVER PLAYER STOLEN BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405013

OVER
7405014

UNDER
Sep 09 2:05 PM
Stream

TYRONE TAYLOR - UNDER/OVER PLAYER STOLEN BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405015

OVER
7405016

UNDER
Sep 09 2:05 PM
Stream

CHRISTIAN YELICH - UNDER/OVER PLAYER STOLEN BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405017

OVER
7405018

UNDER
Sep 09 2:05 PM
Stream

JASSON DOMINGUEZ - UNDER/OVER PLAYER STOLEN BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405019

OVER
7405020

UNDER
Sep 09 2:05 PM
Stream

OSWALD PERAZA - UNDER/OVER PLAYER STOLEN BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405021

OVER
7405022

UNDER
Sep 09 2:05 PM
Stream

GLEYBER TORRES - UNDER/OVER PLAYER STOLEN BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405023

OVER
7405024

UNDER
Sep 09 2:05 PM
Stream

JEFF MCNEIL - UNDER/OVER PLAYER STOLEN BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405025

OVER
7405026

UNDER
Sep 09 2:10 PM
Stream

FRANCISCO LINDOR - UNDER/OVER PLAYER STOLEN BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405027

OVER
7405028

UNDER
Sep 09 2:10 PM
Stream

BRANDON NIMMO - UNDER/OVER PLAYER STOLEN BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405029

OVER
7405030

UNDER
Sep 09 2:10 PM
Stream

JORDAN LUPLOW - UNDER/OVER PLAYER STOLEN BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405031

OVER
7405032

UNDER
Sep 09 2:10 PM
Stream

RONNY MAURICIO - UNDER/OVER PLAYER STOLEN BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405033

OVER
7405034

UNDER
Sep 09 2:10 PM
Stream

BRETT BATY - UNDER/OVER PLAYER STOLEN BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405035

OVER
7405036

UNDER
Sep 09 2:10 PM
Stream

PETER ALONSO - UNDER/OVER PLAYER STOLEN BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405037

OVER
7405038

UNDER
Sep 09 2:10 PM
Stream

MATT WALLNER - UNDER/OVER PLAYER STOLEN BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405039

OVER
7405040

UNDER
Sep 09 2:10 PM
Stream

CARLOS CORREA - UNDER/OVER PLAYER STOLEN BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405041

OVER
7405042

UNDER
Sep 09 2:10 PM
Stream

ROYCE LEWIS - UNDER/OVER PLAYER STOLEN BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405043

OVER
7405044

UNDER
Sep 09 2:10 PM
Stream

RAFAEL ORTEGA - UNDER/OVER PLAYER STOLEN BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405045

OVER
7405046

UNDER
Sep 09 2:10 PM
Stream

JORGE POLANCO - UNDER/OVER PLAYER STOLEN BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405047

OVER
7405048

UNDER
Sep 09 2:10 PM
Stream

WILLI CASTRO - UNDER/OVER PLAYER STOLEN BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405049

OVER
7405050

UNDER
Sep 09 2:10 PM
Stream

KYLE FARMER - UNDER/OVER PLAYER STOLEN BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405051

OVER
7405052

UNDER
Sep 09 2:10 PM
Stream

RYAN JEFFERS - UNDER/OVER PLAYER STOLEN BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405053

OVER
7405054

UNDER
Sep 09 2:10 PM
Stream

NICO HOERNER - UNDER/OVER PLAYER STOLEN BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405055

OVER
7405056

UNDER
Sep 09 2:20 PM
Stream

CORBIN CARROLL - UNDER/OVER PLAYER STOLEN BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405057

OVER
7405058

UNDER
Sep 09 2:20 PM
Stream

KETEL MARTE - UNDER/OVER PLAYER STOLEN BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405059

OVER
7405060

UNDER
Sep 09 2:20 PM
Stream

LOURDES GURRIEL - UNDER/OVER PLAYER STOLEN BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405061

OVER
7405062

UNDER
Sep 09 2:20 PM
Stream

CODY BELLINGER - UNDER/OVER PLAYER STOLEN BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405063

OVER
7405064

UNDER
Sep 09 2:20 PM
Stream

GABRIEL MORENO - UNDER/OVER PLAYER STOLEN BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405065

OVER
7405066

UNDER
Sep 09 2:20 PM
Stream

NICK MADRIGAL - UNDER/OVER PLAYER STOLEN BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405067

OVER
7405068

UNDER
Sep 09 2:20 PM
Stream

SEIYA SUZUKI - UNDER/OVER PLAYER STOLEN BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405069

OVER
7405070

UNDER
Sep 09 2:20 PM
Stream

GERALDO PERDOMO - UNDER/OVER PLAYER STOLEN BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405071

OVER
7405072

UNDER
Sep 09 2:20 PM
Stream

CHRISTIAN WALKER - UNDER/OVER PLAYER STOLEN BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405073

OVER
7405074

UNDER
Sep 09 2:20 PM
Stream

TOMMY PHAM - UNDER/OVER PLAYER STOLEN BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405075

OVER
7405076

UNDER
Sep 09 2:20 PM
Stream

MIKE TAUCHMAN - UNDER/OVER PLAYER STOLEN BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405077

OVER
7405078

UNDER
Sep 09 2:20 PM
Stream

IAN HAPP - UNDER/OVER PLAYER STOLEN BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405079

OVER
7405080

UNDER
Sep 09 2:20 PM
Stream

DANSBY SWANSON - UNDER/OVER PLAYER STOLEN BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405081

OVER
7405082

UNDER
Sep 09 2:20 PM
Stream

JEIMER CANDELARIO - UNDER/OVER PLAYER STOLEN BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405083

OVER
7405084

UNDER
Sep 09 2:20 PM
Stream

DAVID PERALTA - UNDER/OVER PLAYER STOLEN BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405085

OVER
7405086

UNDER
Sep 09 4:05 PM
Stream

JACOB YOUNG - UNDER/OVER PLAYER STOLEN BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405087

OVER
7405088

UNDER
Sep 09 4:05 PM
Stream

FREDDIE FREEMAN - UNDER/OVER PLAYER STOLEN BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405089

OVER
7405090

UNDER
Sep 09 4:05 PM
Stream

WILL SMITH - UNDER/OVER PLAYER STOLEN BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405091

OVER
7405092

UNDER
Sep 09 4:05 PM
Stream

ENRIQUE HERNANDEZ - UNDER/OVER PLAYER STOLEN BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405093

OVER
7405094

UNDER
Sep 09 4:05 PM
Stream

JAMES OUTMAN - UNDER/OVER PLAYER STOLEN BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405095

OVER
7405096

UNDER
Sep 09 4:05 PM
Stream

ALEX CALL - UNDER/OVER PLAYER STOLEN BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405097

OVER
7405098

UNDER
Sep 09 4:05 PM
Stream

JAKE ALU - UNDER/OVER PLAYER STOLEN BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405099

OVER
7405100

UNDER
Sep 09 4:05 PM
Stream

LANE THOMAS - UNDER/OVER PLAYER STOLEN BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405101

OVER
7405102

UNDER
Sep 09 4:05 PM
Stream

KEIBERT RUIZ - UNDER/OVER PLAYER STOLEN BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405103

OVER
7405104

UNDER
Sep 09 4:05 PM
Stream

JASON HEYWARD - UNDER/OVER PLAYER STOLEN BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405105

OVER
7405106

UNDER
Sep 09 4:05 PM
Stream

MIGUEL ROJAS - UNDER/OVER PLAYER STOLEN BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405107

OVER
7405108

UNDER
Sep 09 4:05 PM
Stream

CJ ABRAMS - UNDER/OVER PLAYER STOLEN BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405109

OVER
7405110

UNDER
Sep 09 4:05 PM
Stream

TAYLOR WALLS - UNDER/OVER PLAYER STOLEN BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405111

OVER
7405112

UNDER
Sep 09 4:05 PM
Stream

TEOSCAR HERNÁNDEZ - UNDER/OVER PLAYER STOLEN BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405113

OVER
7405114

UNDER
Sep 09 4:05 PM
Stream

J.P. CRAWFORD - UNDER/OVER PLAYER STOLEN BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405115

OVER
7405116

UNDER
Sep 09 4:05 PM
Stream

LUKE RALEY - UNDER/OVER PLAYER STOLEN BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405117

OVER
7405118

UNDER
Sep 09 4:05 PM
Stream

CHRISTIAN BETHANCOURT - UNDER/OVER PLAYER STOLEN BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405119

OVER
7405120

UNDER
Sep 09 4:05 PM
Stream

BRANDON LOWE - UNDER/OVER PLAYER STOLEN BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405121

OVER
7405122

UNDER
Sep 09 4:05 PM
Stream

JOSH LOWE - UNDER/OVER PLAYER STOLEN BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405123

OVER
7405124

UNDER
Sep 09 4:05 PM
Stream

RANDY AROZARENA - UNDER/OVER PLAYER STOLEN BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405125

OVER
7405126

UNDER
Sep 09 4:05 PM
Stream

JULIO RODRIGUEZ - UNDER/OVER PLAYER STOLEN BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405127

OVER
7405128

UNDER
Sep 09 4:05 PM
Stream

JOSHUA ROJAS - UNDER/OVER PLAYER STOLEN BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405129

OVER
7405130

UNDER
Sep 09 4:05 PM
Stream

JOSE SIRI - UNDER/OVER PLAYER STOLEN BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405131

OVER
7405132

UNDER
Sep 09 4:05 PM
Stream

JAMES MCCANN - UNDER/OVER PLAYER STOLEN BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405133

OVER
7405134

UNDER
Sep 09 4:10 PM
Stream

ANTHONY SANTANDER - UNDER/OVER PLAYER STOLEN BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405135

OVER
7405136

UNDER
Sep 09 4:10 PM
Stream

RAFAEL DEVERS - UNDER/OVER PLAYER STOLEN BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405137

OVER
7405138

UNDER
Sep 09 4:10 PM
Stream

JORGE MATEO - UNDER/OVER PLAYER STOLEN BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405139

OVER
7405140

UNDER
Sep 09 4:10 PM
Stream

TREVOR STORY - UNDER/OVER PLAYER STOLEN BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405141

OVER
7405142

UNDER
Sep 09 4:10 PM
Stream

RAMON URIAS - UNDER/OVER PLAYER STOLEN BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405143

OVER
7405144

UNDER
Sep 09 4:10 PM
Stream

CONNOR WONG - UNDER/OVER PLAYER STOLEN BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405145

OVER
7405146

UNDER
Sep 09 4:10 PM
Stream

ALEX VERDUGO - UNDER/OVER PLAYER STOLEN BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405147

OVER
7405148

UNDER
Sep 09 4:10 PM
Stream

ADLEY RUTSCHMAN - UNDER/OVER PLAYER STOLEN BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405149

OVER
7405150

UNDER
Sep 09 4:10 PM
Stream

AARON HICKS - UNDER/OVER PLAYER STOLEN BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405151

OVER
7405152

UNDER
Sep 09 4:10 PM
Stream

ADAM DUVALL - UNDER/OVER PLAYER STOLEN BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405153

OVER
7405154

UNDER
Sep 09 4:10 PM
Stream

RYAN MOUNTCASTLE - UNDER/OVER PLAYER STOLEN BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405155

OVER
7405156

UNDER
Sep 09 4:10 PM
Stream

GUNNAR HENDERSON - UNDER/OVER PLAYER STOLEN BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405157

OVER
7405158

UNDER
Sep 09 4:10 PM
Stream

MASATAKA YOSHIDA - UNDER/OVER PLAYER STOLEN BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405159

OVER
7405160

UNDER
Sep 09 4:10 PM
Stream

AUSTIN HAYS - UNDER/OVER PLAYER STOLEN BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405161

OVER
7405162

UNDER
Sep 09 4:10 PM
Stream

NICK FORTES - UNDER/OVER PLAYER STOLEN BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405163

OVER
7405164

UNDER
Sep 09 6:05 PM
Stream

JAKE CAVE - UNDER/OVER PLAYER STOLEN BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405165

OVER
7405166

UNDER
Sep 09 6:05 PM
Stream

BRYAN DE LA CRUZ - UNDER/OVER PLAYER STOLEN BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405167

OVER
7405168

UNDER
Sep 09 6:05 PM
Stream

JESUS SANCHEZ - UNDER/OVER PLAYER STOLEN BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405169

OVER
7405170

UNDER
Sep 09 6:05 PM
Stream

JACOB MICHAEL BURGER - UNDER/OVER PLAYER STOLEN BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405171

OVER
7405172

UNDER
Sep 09 6:05 PM
Stream

NICK CASTELLANOS - UNDER/OVER PLAYER STOLEN BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405173

OVER
7405174

UNDER
Sep 09 6:05 PM
Stream

LUIS ARRAEZ - UNDER/OVER PLAYER STOLEN BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405175

OVER
7405176

UNDER
Sep 09 6:05 PM
Stream

BRANDON MARSH - UNDER/OVER PLAYER STOLEN BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405177

OVER
7405178

UNDER
Sep 09 6:05 PM
Stream

BRYSON STOTT - UNDER/OVER PLAYER STOLEN BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405179

OVER
7405180

UNDER
Sep 09 6:05 PM
Stream

BRYCE HARPER - UNDER/OVER PLAYER STOLEN BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405181

OVER
7405182

UNDER
Sep 09 6:05 PM
Stream

JAZZ CHISHOLM - UNDER/OVER PLAYER STOLEN BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405183

OVER
7405184

UNDER
Sep 09 6:05 PM
Stream

JOEY WENDLE - UNDER/OVER PLAYER STOLEN BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405185

OVER
7405186

UNDER
Sep 09 6:05 PM
Stream

TREA TURNER - UNDER/OVER PLAYER STOLEN BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405187

OVER
7405188

UNDER
Sep 09 6:05 PM
Stream

ALEC BOHM - UNDER/OVER PLAYER STOLEN BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405189

OVER
7405190

UNDER
Sep 09 6:05 PM
Stream

KYLE SCHWARBER - UNDER/OVER PLAYER STOLEN BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405191

OVER
7405192

UNDER
Sep 09 6:05 PM
Stream

J.T. REALMUTO - UNDER/OVER PLAYER STOLEN BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405193

OVER
7405194

UNDER
Sep 09 6:05 PM
Stream

NOLAN ARENADO - UNDER/OVER PLAYER STOLEN BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405195

OVER
7405196

UNDER
Sep 09 6:40 PM
Stream

NICK SENZEL - UNDER/OVER PLAYER STOLEN BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405197

OVER
7405198

UNDER
Sep 09 6:40 PM
Stream

TYLER O'NEILL - UNDER/OVER PLAYER STOLEN BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405199

OVER
7405200

UNDER
Sep 09 6:40 PM
Stream

PAUL GOLDSCHMIDT - UNDER/OVER PLAYER STOLEN BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405201

OVER
7405202

UNDER
Sep 09 6:40 PM
Stream

SPENCER STEER - UNDER/OVER PLAYER STOLEN BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405203

OVER
7405204

UNDER
Sep 09 6:40 PM
Stream

WILLSON CONTRERAS - UNDER/OVER PLAYER STOLEN BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405205

OVER
7405206

UNDER
Sep 09 6:40 PM
Stream

JORDAN WALKER - UNDER/OVER PLAYER STOLEN BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405207

OVER
7405208

UNDER
Sep 09 6:40 PM
Stream

ELLY DE LA CRUZ - UNDER/OVER PLAYER STOLEN BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405209

OVER
7405210

UNDER
Sep 09 6:40 PM
Stream

MASYN WINN - UNDER/OVER PLAYER STOLEN BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405211

OVER
7405212

UNDER
Sep 09 6:40 PM
Stream

NOLAN GORMAN - UNDER/OVER PLAYER STOLEN BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405213

OVER
7405214

UNDER
Sep 09 6:40 PM
Stream

TOMMY EDMAN - UNDER/OVER PLAYER STOLEN BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405215

OVER
7405216

UNDER
Sep 09 6:40 PM
Stream

LARS NOOTBAAR - UNDER/OVER PLAYER STOLEN BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405217

OVER
7405218

UNDER
Sep 09 6:40 PM
Stream

NOELVI MARTE - UNDER/OVER PLAYER STOLEN BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405219

OVER
7405220

UNDER
Sep 09 6:40 PM
Stream

STUART FAIRCHILD - UNDER/OVER PLAYER STOLEN BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405221

OVER
7405222

UNDER
Sep 09 6:40 PM
Stream

HARRISON BADER - UNDER/OVER PLAYER STOLEN BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405223

OVER
7405224

UNDER
Sep 09 6:40 PM
Stream

MANNY MACHADO - UNDER/OVER PLAYER STOLEN BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405225

OVER
7405226

UNDER
Sep 09 7:10 PM
Stream

JUAN SOTO - UNDER/OVER PLAYER STOLEN BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405227

OVER
7405228

UNDER
Sep 09 7:10 PM
Stream

JEREMY PENA - UNDER/OVER PLAYER STOLEN BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405229

OVER
7405230

UNDER
Sep 09 7:10 PM
Stream

TRENT GRISHAM - UNDER/OVER PLAYER STOLEN BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405231

OVER
7405232

UNDER
Sep 09 7:10 PM
Stream

XANDER BOGAERTS - UNDER/OVER PLAYER STOLEN BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405233

OVER
7405234

UNDER
Sep 09 7:10 PM
Stream

MICHAEL BRANTLEY - UNDER/OVER PLAYER STOLEN BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405235

OVER
7405236

UNDER
Sep 09 7:10 PM
Stream

HA-SEONG KIM - UNDER/OVER PLAYER STOLEN BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405237

OVER
7405238

UNDER
Sep 09 7:10 PM
Stream

MAURICIO DUBÓN - UNDER/OVER PLAYER STOLEN BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405239

OVER
7405240

UNDER
Sep 09 7:10 PM
Stream

KYLE TUCKER - UNDER/OVER PLAYER STOLEN BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405241

OVER
7405242

UNDER
Sep 09 7:10 PM
Stream

JOSE ALTUVE - UNDER/OVER PLAYER STOLEN BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405243

OVER
7405244

UNDER
Sep 09 7:10 PM
Stream

FERNANDO TATIS JR. - UNDER/OVER PLAYER STOLEN BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405245

OVER
7405246

UNDER
Sep 09 7:10 PM
Stream

RONALD ACUNA - UNDER/OVER PLAYER STOLEN BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405247

OVER
7405248

UNDER
Sep 09 7:20 PM
Stream

LIOVER PEGUERO - UNDER/OVER PLAYER STOLEN BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405249

OVER
7405250

UNDER
Sep 09 7:20 PM
Stream

JI-HWAN BAE - UNDER/OVER PLAYER STOLEN BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405251

OVER
7405252

UNDER
Sep 09 7:20 PM
Stream

EDDIE ROSARIO - UNDER/OVER PLAYER STOLEN BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405253

OVER
7405254

UNDER
Sep 09 7:20 PM
Stream

BRYAN REYNOLDS - UNDER/OVER PLAYER STOLEN BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405255

OVER
7405256

UNDER
Sep 09 7:20 PM
Stream

MIGUEL ANDÚJAR - UNDER/OVER PLAYER STOLEN BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405257

OVER
7405258

UNDER
Sep 09 7:20 PM
Stream

MICHAEL HARRIS - UNDER/OVER PLAYER STOLEN BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405259

OVER
7405260

UNDER
Sep 09 7:20 PM
Stream

OZZIE ALBIES - UNDER/OVER PLAYER STOLEN BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405261

OVER
7405262

UNDER
Sep 09 7:20 PM
Stream

JARED TRIOLO - UNDER/OVER PLAYER STOLEN BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405263

OVER
7405264

UNDER
Sep 09 7:20 PM
Stream

ALIKA WILLIAMS - UNDER/OVER PLAYER STOLEN BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405265

OVER
7405266

UNDER
Sep 09 7:20 PM
Stream

KE'BRYAN HAYES - UNDER/OVER PLAYER STOLEN BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405267

OVER
7405268

UNDER
Sep 09 7:20 PM
Stream

CONNOR JOE - UNDER/OVER PLAYER STOLEN BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405269

OVER
7405270

UNDER
Sep 09 7:20 PM
Stream

RYAN MCMAHON - UNDER/OVER PLAYER STOLEN BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405271

OVER
7405272

UNDER
Sep 09 9:05 PM
Stream

NOLAN JONES - UNDER/OVER PLAYER STOLEN BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405273

OVER
7405274

UNDER
Sep 09 9:05 PM
Stream

MIKE YASTRZEMSKI - UNDER/OVER PLAYER STOLEN BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405275

OVER
7405276

UNDER
Sep 09 9:05 PM
Stream

BLAKE SABOL - UNDER/OVER PLAYER STOLEN BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405277

OVER
7405278

UNDER
Sep 09 9:05 PM
Stream

EZEQUIEL TOVAR - UNDER/OVER PLAYER STOLEN BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405279

OVER
7405280

UNDER
Sep 09 9:05 PM
Stream

THAIRO ESTRADA - UNDER/OVER PLAYER STOLEN BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405281

OVER
7405282

UNDER
Sep 09 9:05 PM
Stream

CHARLIE BLACKMON - UNDER/OVER PLAYER STOLEN BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405283

OVER
7405284

UNDER
Sep 09 9:05 PM
Stream

BRENTON DOYLE - UNDER/OVER PLAYER STOLEN BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405285

OVER
7405286

UNDER
Sep 09 9:05 PM
Stream

GABRIEL ARIAS - UNDER/OVER PLAYER STOLEN BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405287

OVER
7405288

UNDER
Sep 09 9:07 PM
Stream

KOLE CALHOUN - UNDER/OVER PLAYER STOLEN BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405289

OVER
7405290

UNDER
Sep 09 9:07 PM
Stream

JOSE RAMIREZ - UNDER/OVER PLAYER STOLEN BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405291

OVER
7405292

UNDER
Sep 09 9:07 PM
Stream

JOSH NAYLOR - UNDER/OVER PLAYER STOLEN BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405293

OVER
7405294

UNDER
Sep 09 9:07 PM
Stream

RANDAL GRICHUK - UNDER/OVER PLAYER STOLEN BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405295

OVER
7405296

UNDER
Sep 09 9:07 PM
Stream

MYLES STRAW - UNDER/OVER PLAYER STOLEN BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405297

OVER
7405298

UNDER
Sep 09 9:07 PM
Stream

KYREN PARIS - UNDER/OVER PLAYER STOLEN BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405299

OVER
7405300

UNDER
Sep 09 9:07 PM
Stream

NOLAN SCHANUEL - UNDER/OVER PLAYER STOLEN BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405301

OVER
7405302

UNDER
Sep 09 9:07 PM
Stream

STEVEN KWAN - UNDER/OVER PLAYER STOLEN BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405303

OVER
7405304

UNDER
Sep 09 9:07 PM
Stream

RAMON LAUREANO - UNDER/OVER PLAYER STOLEN BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405305

OVER
7405306

UNDER
Sep 09 9:07 PM
Stream

ANDRES GIMENEZ - UNDER/OVER PLAYER STOLEN BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405307

OVER
7405308

UNDER
Sep 09 9:07 PM
Stream

BOBBY WITT JR. - UNDER/OVER PLAYER STOLEN BASES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405309

OVER
7405310

UNDER
Sep 09 3:07 PM
Stream

MICHAEL MASSEY - UNDER/OVER PLAYER STOLEN BASES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405311

OVER
7405312

UNDER
Sep 09 3:07 PM
Stream

DREW WATERS - UNDER/OVER PLAYER STOLEN BASES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405313

OVER
7405314

UNDER
Sep 09 3:07 PM
Stream

MAIKEL GARCIA - UNDER/OVER PLAYER STOLEN BASES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405315

OVER
7405316

UNDER
Sep 09 3:07 PM
Stream

MJ MELENDEZ - UNDER/OVER PLAYER STOLEN BASES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7405317

OVER
7405318

UNDER
Sep 09 3:07 PM
Stream

MLB - PLAYER TOTAL RUNS
OSWALD PERAZA - UNDER/OVER PLAYER RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406003

OVER
7406004

UNDER
Sep 09 2:05 PM
Stream

DAVID JOHN LEMAHIEU - UNDER/OVER PLAYER RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406005

OVER
7406006

UNDER
Sep 09 2:05 PM
Stream

GIANCARLO STANTON - UNDER/OVER PLAYER RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406007

OVER
7406008

UNDER
Sep 09 2:05 PM
Stream

ANTHONY VOLPE - UNDER/OVER PLAYER RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406009

OVER
7406010

UNDER
Sep 09 2:05 PM
Stream

AARON JUDGE - UNDER/OVER PLAYER RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406011

OVER
7406012

UNDER
Sep 09 2:05 PM
Stream

WILLIAM CONTRERAS - UNDER/OVER PLAYER RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406013

OVER
7406014

UNDER
Sep 09 2:05 PM
Stream

CHRISTIAN YELICH - UNDER/OVER PLAYER RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406015

OVER
7406016

UNDER
Sep 09 2:05 PM
Stream

JASSON DOMINGUEZ - UNDER/OVER PLAYER RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406017

OVER
7406018

UNDER
Sep 09 2:05 PM
Stream

KYLE HIGASHIOKA - UNDER/OVER PLAYER RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406019

OVER
7406020

UNDER
Sep 09 2:05 PM
Stream

AUSTIN WELLS - UNDER/OVER PLAYER RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406021

OVER
7406022

UNDER
Sep 09 2:05 PM
Stream

GLEYBER TORRES - UNDER/OVER PLAYER RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406023

OVER
7406024

UNDER
Sep 09 2:05 PM
Stream

SAL FRELICK - UNDER/OVER PLAYER RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406025

OVER
7406026

UNDER
Sep 09 2:05 PM
Stream

ANDRUW MONASTERIO - UNDER/OVER PLAYER RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406027

OVER
7406028

UNDER
Sep 09 2:05 PM
Stream

TYRONE TAYLOR - UNDER/OVER PLAYER RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406029

OVER
7406030

UNDER
Sep 09 2:05 PM
Stream

WILLY ADAMES - UNDER/OVER PLAYER RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406031

OVER
7406032

UNDER
Sep 09 2:05 PM
Stream

BRICE TURANG - UNDER/OVER PLAYER RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406033

OVER
7406034

UNDER
Sep 09 2:05 PM
Stream

MARK VIENTOS - UNDER/OVER PLAYER RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406035

OVER
7406036

UNDER
Sep 09 2:10 PM
Stream

OMAR NARVAEZ - UNDER/OVER PLAYER RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406037

OVER
7406038

UNDER
Sep 09 2:10 PM
Stream

ROYCE LEWIS - UNDER/OVER PLAYER RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406039

OVER
7406040

UNDER
Sep 09 2:10 PM
Stream

RONNY MAURICIO - UNDER/OVER PLAYER RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406041

OVER
7406042

UNDER
Sep 09 2:10 PM
Stream

BRANDON NIMMO - UNDER/OVER PLAYER RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406043

OVER
7406044

UNDER
Sep 09 2:10 PM
Stream

CARLOS CORREA - UNDER/OVER PLAYER RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406045

OVER
7406046

UNDER
Sep 09 2:10 PM
Stream

RAFAEL ORTEGA - UNDER/OVER PLAYER RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406047

OVER
7406048

UNDER
Sep 09 2:10 PM
Stream

MATT WALLNER - UNDER/OVER PLAYER RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406049

OVER
7406050

UNDER
Sep 09 2:10 PM
Stream

PETER ALONSO - UNDER/OVER PLAYER RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406051

OVER
7406052

UNDER
Sep 09 2:10 PM
Stream

KYLE FARMER - UNDER/OVER PLAYER RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406053

OVER
7406054

UNDER
Sep 09 2:10 PM
Stream

RYAN JEFFERS - UNDER/OVER PLAYER RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406055

OVER
7406056

UNDER
Sep 09 2:10 PM
Stream

FRANCISCO LINDOR - UNDER/OVER PLAYER RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406057

OVER
7406058

UNDER
Sep 09 2:10 PM
Stream

JEFF MCNEIL - UNDER/OVER PLAYER RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406059

OVER
7406060

UNDER
Sep 09 2:10 PM
Stream

BRETT BATY - UNDER/OVER PLAYER RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406061

OVER
7406062

UNDER
Sep 09 2:10 PM
Stream

JORGE POLANCO - UNDER/OVER PLAYER RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406063

OVER
7406064

UNDER
Sep 09 2:10 PM
Stream

JORDAN LUPLOW - UNDER/OVER PLAYER RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406065

OVER
7406066

UNDER
Sep 09 2:10 PM
Stream

DONOVAN SOLANO - UNDER/OVER PLAYER RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406067

OVER
7406068

UNDER
Sep 09 2:10 PM
Stream

WILLI CASTRO - UNDER/OVER PLAYER RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406069

OVER
7406070

UNDER
Sep 09 2:10 PM
Stream

JEIMER CANDELARIO - UNDER/OVER PLAYER RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406071

OVER
7406072

UNDER
Sep 09 2:20 PM
Stream

KETEL MARTE - UNDER/OVER PLAYER RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406073

OVER
7406074

UNDER
Sep 09 2:20 PM
Stream

NICO HOERNER - UNDER/OVER PLAYER RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406075

OVER
7406076

UNDER
Sep 09 2:20 PM
Stream

YAN GOMES - UNDER/OVER PLAYER RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406077

OVER
7406078

UNDER
Sep 09 2:20 PM
Stream

GABRIEL MORENO - UNDER/OVER PLAYER RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406079

OVER
7406080

UNDER
Sep 09 2:20 PM
Stream

LOURDES GURRIEL - UNDER/OVER PLAYER RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406081

OVER
7406082

UNDER
Sep 09 2:20 PM
Stream

IAN HAPP - UNDER/OVER PLAYER RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406083

OVER
7406084

UNDER
Sep 09 2:20 PM
Stream

CHRISTIAN WALKER - UNDER/OVER PLAYER RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406085

OVER
7406086

UNDER
Sep 09 2:20 PM
Stream

CODY BELLINGER - UNDER/OVER PLAYER RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406087

OVER
7406088

UNDER
Sep 09 2:20 PM
Stream

EVAN LONGORIA - UNDER/OVER PLAYER RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406089

OVER
7406090

UNDER
Sep 09 2:20 PM
Stream

EMMANUEL RIVERA - UNDER/OVER PLAYER RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406091

OVER
7406092

UNDER
Sep 09 2:20 PM
Stream

GERALDO PERDOMO - UNDER/OVER PLAYER RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406093

OVER
7406094

UNDER
Sep 09 2:20 PM
Stream

MIKE TAUCHMAN - UNDER/OVER PLAYER RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406095

OVER
7406096

UNDER
Sep 09 2:20 PM
Stream

SEIYA SUZUKI - UNDER/OVER PLAYER RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406097

OVER
7406098

UNDER
Sep 09 2:20 PM
Stream

DANSBY SWANSON - UNDER/OVER PLAYER RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406099

OVER
7406100

UNDER
Sep 09 2:20 PM
Stream

NICK MADRIGAL - UNDER/OVER PLAYER RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406101

OVER
7406102

UNDER
Sep 09 2:20 PM
Stream

TOMMY PHAM - UNDER/OVER PLAYER RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406103

OVER
7406104

UNDER
Sep 09 2:20 PM
Stream

CORBIN CARROLL - UNDER/OVER PLAYER RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406105

OVER
7406106

UNDER
Sep 09 2:20 PM
Stream

JAMES OUTMAN - UNDER/OVER PLAYER RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406107

OVER
7406108

UNDER
Sep 09 4:05 PM
Stream

MAX MUNCY - UNDER/OVER PLAYER RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406109

OVER
7406110

UNDER
Sep 09 4:05 PM
Stream

MIGUEL ROJAS - UNDER/OVER PLAYER RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406111

OVER
7406112

UNDER
Sep 09 4:05 PM
Stream

FREDDIE FREEMAN - UNDER/OVER PLAYER RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406113

OVER
7406114

UNDER
Sep 09 4:05 PM
Stream

JASON HEYWARD - UNDER/OVER PLAYER RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406115

OVER
7406116

UNDER
Sep 09 4:05 PM
Stream

JAKE ALU - UNDER/OVER PLAYER RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406117

OVER
7406118

UNDER
Sep 09 4:05 PM
Stream

ENRIQUE HERNANDEZ - UNDER/OVER PLAYER RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406119

OVER
7406120

UNDER
Sep 09 4:05 PM
Stream

ALEX CALL - UNDER/OVER PLAYER RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406121

OVER
7406122

UNDER
Sep 09 4:05 PM
Stream

WILL SMITH - UNDER/OVER PLAYER RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406123

OVER
7406124

UNDER
Sep 09 4:05 PM
Stream

JACOB YOUNG - UNDER/OVER PLAYER RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406125

OVER
7406126

UNDER
Sep 09 4:05 PM
Stream

DAVID PERALTA - UNDER/OVER PLAYER RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406127

OVER
7406128

UNDER
Sep 09 4:05 PM
Stream

CJ ABRAMS - UNDER/OVER PLAYER RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406129

OVER
7406130

UNDER
Sep 09 4:05 PM
Stream

CARTER KIEBOOM - UNDER/OVER PLAYER RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406131

OVER
7406132

UNDER
Sep 09 4:05 PM
Stream

LANE THOMAS - UNDER/OVER PLAYER RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406133

OVER
7406134

UNDER
Sep 09 4:05 PM
Stream

KEIBERT RUIZ - UNDER/OVER PLAYER RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406135

OVER
7406136

UNDER
Sep 09 4:05 PM
Stream

J.D. MARTINEZ - UNDER/OVER PLAYER RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406137

OVER
7406138

UNDER
Sep 09 4:05 PM
Stream

DOMINIC SMITH - UNDER/OVER PLAYER RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406139

OVER
7406140

UNDER
Sep 09 4:05 PM
Stream

JOEY MENESES - UNDER/OVER PLAYER RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406141

OVER
7406142

UNDER
Sep 09 4:05 PM
Stream

TAYLOR WALLS - UNDER/OVER PLAYER RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406143

OVER
7406144

UNDER
Sep 09 4:05 PM
Stream

RANDY AROZARENA - UNDER/OVER PLAYER RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406145

OVER
7406146

UNDER
Sep 09 4:05 PM
Stream

EUGENIO SUAREZ - UNDER/OVER PLAYER RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406147

OVER
7406148

UNDER
Sep 09 4:05 PM
Stream

TY FRANCE - UNDER/OVER PLAYER RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406149

OVER
7406150

UNDER
Sep 09 4:05 PM
Stream

BRANDON LOWE - UNDER/OVER PLAYER RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406151

OVER
7406152

UNDER
Sep 09 4:05 PM
Stream

DOMINIC CANZONE - UNDER/OVER PLAYER RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406153

OVER
7406154

UNDER
Sep 09 4:05 PM
Stream

TEOSCAR HERNÁNDEZ - UNDER/OVER PLAYER RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406155

OVER
7406156

UNDER
Sep 09 4:05 PM
Stream

JOSHUA ROJAS - UNDER/OVER PLAYER RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406157

OVER
7406158

UNDER
Sep 09 4:05 PM
Stream

JOSH LOWE - UNDER/OVER PLAYER RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406159

OVER
7406160

UNDER
Sep 09 4:05 PM
Stream

ISAAC PAREDES - UNDER/OVER PLAYER RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406161

OVER
7406162

UNDER
Sep 09 4:05 PM
Stream

CHRISTIAN BETHANCOURT - UNDER/OVER PLAYER RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406163

OVER
7406164

UNDER
Sep 09 4:05 PM
Stream

JOSE SIRI - UNDER/OVER PLAYER RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406165

OVER
7406166

UNDER
Sep 09 4:05 PM
Stream

LUKE RALEY - UNDER/OVER PLAYER RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406167

OVER
7406168

UNDER
Sep 09 4:05 PM
Stream

J.P. CRAWFORD - UNDER/OVER PLAYER RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406169

OVER
7406170

UNDER
Sep 09 4:05 PM
Stream

MIKE FORD - UNDER/OVER PLAYER RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406171

OVER
7406172

UNDER
Sep 09 4:05 PM
Stream

CAL RALEIGH - UNDER/OVER PLAYER RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406173

OVER
7406174

UNDER
Sep 09 4:05 PM
Stream

YANDY DIAZ - UNDER/OVER PLAYER RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406175

OVER
7406176

UNDER
Sep 09 4:05 PM
Stream

ANTHONY SANTANDER - UNDER/OVER PLAYER RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406177

OVER
7406178

UNDER
Sep 09 4:10 PM
Stream

RAFAEL DEVERS - UNDER/OVER PLAYER RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406179

OVER
7406180

UNDER
Sep 09 4:10 PM
Stream

JORGE MATEO - UNDER/OVER PLAYER RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406181

OVER
7406182

UNDER
Sep 09 4:10 PM
Stream

RYAN MOUNTCASTLE - UNDER/OVER PLAYER RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406183

OVER
7406184

UNDER
Sep 09 4:10 PM
Stream

AUSTIN HAYS - UNDER/OVER PLAYER RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406185

OVER
7406186

UNDER
Sep 09 4:10 PM
Stream

JAMES MCCANN - UNDER/OVER PLAYER RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406187

OVER
7406188

UNDER
Sep 09 4:10 PM
Stream

TREVOR STORY - UNDER/OVER PLAYER RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406189

OVER
7406190

UNDER
Sep 09 4:10 PM
Stream

ALEX VERDUGO - UNDER/OVER PLAYER RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406191

OVER
7406192

UNDER
Sep 09 4:10 PM
Stream

GUNNAR HENDERSON - UNDER/OVER PLAYER RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406193

OVER
7406194

UNDER
Sep 09 4:10 PM
Stream

ADAM DUVALL - UNDER/OVER PLAYER RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406195

OVER
7406196

UNDER
Sep 09 4:10 PM
Stream

ADLEY RUTSCHMAN - UNDER/OVER PLAYER RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406197

OVER
7406198

UNDER
Sep 09 4:10 PM
Stream

RAMON URIAS - UNDER/OVER PLAYER RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406199

OVER
7406200

UNDER
Sep 09 4:10 PM
Stream

MASATAKA YOSHIDA - UNDER/OVER PLAYER RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406201

OVER
7406202

UNDER
Sep 09 4:10 PM
Stream

AARON HICKS - UNDER/OVER PLAYER RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406203

OVER
7406204

UNDER
Sep 09 4:10 PM
Stream

JUSTIN TURNER - UNDER/OVER PLAYER RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406205

OVER
7406206

UNDER
Sep 09 4:10 PM
Stream

CONNOR WONG - UNDER/OVER PLAYER RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406207

OVER
7406208

UNDER
Sep 09 4:10 PM
Stream

TRISTON CASAS - UNDER/OVER PLAYER RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406209

OVER
7406210

UNDER
Sep 09 4:10 PM
Stream

BRYCE HARPER - UNDER/OVER PLAYER RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406211

OVER
7406212

UNDER
Sep 09 6:05 PM
Stream

TREA TURNER - UNDER/OVER PLAYER RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406213

OVER
7406214

UNDER
Sep 09 6:05 PM
Stream

BRANDON MARSH - UNDER/OVER PLAYER RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406215

OVER
7406216

UNDER
Sep 09 6:05 PM
Stream

JOEY WENDLE - UNDER/OVER PLAYER RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406217

OVER
7406218

UNDER
Sep 09 6:05 PM
Stream

KYLE SCHWARBER - UNDER/OVER PLAYER RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406219

OVER
7406220

UNDER
Sep 09 6:05 PM
Stream

JESUS SANCHEZ - UNDER/OVER PLAYER RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406221

OVER
7406222

UNDER
Sep 09 6:05 PM
Stream

BRYSON STOTT - UNDER/OVER PLAYER RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406223

OVER
7406224

UNDER
Sep 09 6:05 PM
Stream

JOSHUA EVAN BELL - UNDER/OVER PLAYER RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406225

OVER
7406226

UNDER
Sep 09 6:05 PM
Stream

BRYAN DE LA CRUZ - UNDER/OVER PLAYER RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406227

OVER
7406228

UNDER
Sep 09 6:05 PM
Stream

LUIS ARRAEZ - UNDER/OVER PLAYER RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406229

OVER
7406230

UNDER
Sep 09 6:05 PM
Stream

JAZZ CHISHOLM - UNDER/OVER PLAYER RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406231

OVER
7406232

UNDER
Sep 09 6:05 PM
Stream

JACOB MICHAEL BURGER - UNDER/OVER PLAYER RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406233

OVER
7406234

UNDER
Sep 09 6:05 PM
Stream

JAKE CAVE - UNDER/OVER PLAYER RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406235

OVER
7406236

UNDER
Sep 09 6:05 PM
Stream

J.T. REALMUTO - UNDER/OVER PLAYER RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406237

OVER
7406238

UNDER
Sep 09 6:05 PM
Stream

NICK FORTES - UNDER/OVER PLAYER RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406239

OVER
7406240

UNDER
Sep 09 6:05 PM
Stream

ALEC BOHM - UNDER/OVER PLAYER RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406241

OVER
7406242

UNDER
Sep 09 6:05 PM
Stream

NICK CASTELLANOS - UNDER/OVER PLAYER RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406243

OVER
7406244

UNDER
Sep 09 6:05 PM
Stream

LARS NOOTBAAR - UNDER/OVER PLAYER RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406245

OVER
7406246

UNDER
Sep 09 6:40 PM
Stream

STUART FAIRCHILD - UNDER/OVER PLAYER RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406247

OVER
7406248

UNDER
Sep 09 6:40 PM
Stream

NOELVI MARTE - UNDER/OVER PLAYER RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406249

OVER
7406250

UNDER
Sep 09 6:40 PM
Stream

HUNTER RENFROE - UNDER/OVER PLAYER RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406251

OVER
7406252

UNDER
Sep 09 6:40 PM
Stream

MASYN WINN - UNDER/OVER PLAYER RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406253

OVER
7406254

UNDER
Sep 09 6:40 PM
Stream

NOLAN GORMAN - UNDER/OVER PLAYER RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406255

OVER
7406256

UNDER
Sep 09 6:40 PM
Stream

PAUL GOLDSCHMIDT - UNDER/OVER PLAYER RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406257

OVER
7406258

UNDER
Sep 09 6:40 PM
Stream

CHRISTIAN ENCARNACION-STRAND - UNDER/OVER PLAYER RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406259

OVER
7406260

UNDER
Sep 09 6:40 PM
Stream

ELLY DE LA CRUZ - UNDER/OVER PLAYER RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406261

OVER
7406262

UNDER
Sep 09 6:40 PM
Stream

NOLAN ARENADO - UNDER/OVER PLAYER RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406263

OVER
7406264

UNDER
Sep 09 6:40 PM
Stream

TYLER O'NEILL - UNDER/OVER PLAYER RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406265

OVER
7406266

UNDER
Sep 09 6:40 PM
Stream

TYLER STEPHENSON - UNDER/OVER PLAYER RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406267

OVER
7406268

UNDER
Sep 09 6:40 PM
Stream

SPENCER STEER - UNDER/OVER PLAYER RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406269

OVER
7406270

UNDER
Sep 09 6:40 PM
Stream

WILLSON CONTRERAS - UNDER/OVER PLAYER RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406271

OVER
7406272

UNDER
Sep 09 6:40 PM
Stream

NICK SENZEL - UNDER/OVER PLAYER RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406273

OVER
7406274

UNDER
Sep 09 6:40 PM
Stream

JORDAN WALKER - UNDER/OVER PLAYER RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406275

OVER
7406276

UNDER
Sep 09 6:40 PM
Stream

HARRISON BADER - UNDER/OVER PLAYER RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406277

OVER
7406278

UNDER
Sep 09 6:40 PM
Stream

TOMMY EDMAN - UNDER/OVER PLAYER RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406279

OVER
7406280

UNDER
Sep 09 6:40 PM
Stream

MATTHEW BATTEN - UNDER/OVER PLAYER RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406281

OVER
7406282

UNDER
Sep 09 7:10 PM
Stream

KYLE TUCKER - UNDER/OVER PLAYER RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406283

OVER
7406284

UNDER
Sep 09 7:10 PM
Stream

GARRETT COOPER - UNDER/OVER PLAYER RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406285

OVER
7406286

UNDER
Sep 09 7:10 PM
Stream

TRENT GRISHAM - UNDER/OVER PLAYER RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406287

OVER
7406288

UNDER
Sep 09 7:10 PM
Stream

FERNANDO TATIS JR. - UNDER/OVER PLAYER RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406289

OVER
7406290

UNDER
Sep 09 7:10 PM
Stream

MARTIN MALDONADO - UNDER/OVER PLAYER RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406291

OVER
7406292

UNDER
Sep 09 7:10 PM
Stream

MICHAEL BRANTLEY - UNDER/OVER PLAYER RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406293

OVER
7406294

UNDER
Sep 09 7:10 PM
Stream

XANDER BOGAERTS - UNDER/OVER PLAYER RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406295

OVER
7406296

UNDER
Sep 09 7:10 PM
Stream

LUIS CAMPUSANO - UNDER/OVER PLAYER RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406297

OVER
7406298

UNDER
Sep 09 7:10 PM
Stream

JUAN SOTO - UNDER/OVER PLAYER RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406299

OVER
7406300

UNDER
Sep 09 7:10 PM
Stream

MANNY MACHADO - UNDER/OVER PLAYER RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406301

OVER
7406302

UNDER
Sep 09 7:10 PM
Stream

JOSE ABREU - UNDER/OVER PLAYER RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406303

OVER
7406304

UNDER
Sep 09 7:10 PM
Stream

ALEX BREGMAN - UNDER/OVER PLAYER RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406305

OVER
7406306

UNDER
Sep 09 7:10 PM
Stream

JEREMY PENA - UNDER/OVER PLAYER RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406307

OVER
7406308

UNDER
Sep 09 7:10 PM
Stream

MAURICIO DUBÓN - UNDER/OVER PLAYER RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406309

OVER
7406310

UNDER
Sep 09 7:10 PM
Stream

JOSE ALTUVE - UNDER/OVER PLAYER RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406311

OVER
7406312

UNDER
Sep 09 7:10 PM
Stream

HA-SEONG KIM - UNDER/OVER PLAYER RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406313

OVER
7406314

UNDER
Sep 09 7:10 PM
Stream

YORDAN ALVAREZ - UNDER/OVER PLAYER RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406315

OVER
7406316

UNDER
Sep 09 7:10 PM
Stream

MIGUEL ANDÚJAR - UNDER/OVER PLAYER RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406317

OVER
7406318

UNDER
Sep 09 7:20 PM
Stream

ALIKA WILLIAMS - UNDER/OVER PLAYER RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406319

OVER
7406320

UNDER
Sep 09 7:20 PM
Stream

ENDY RODRIGUEZ - UNDER/OVER PLAYER RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406321

OVER
7406322

UNDER
Sep 09 7:20 PM
Stream

AUSTIN RILEY - UNDER/OVER PLAYER RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406323

OVER
7406324

UNDER
Sep 09 7:20 PM
Stream

EDDIE ROSARIO - UNDER/OVER PLAYER RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406325

OVER
7406326

UNDER
Sep 09 7:20 PM
Stream

MICHAEL HARRIS - UNDER/OVER PLAYER RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406327

OVER
7406328

UNDER
Sep 09 7:20 PM
Stream

JARED TRIOLO - UNDER/OVER PLAYER RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406329

OVER
7406330

UNDER
Sep 09 7:20 PM
Stream

OZZIE ALBIES - UNDER/OVER PLAYER RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406331

OVER
7406332

UNDER
Sep 09 7:20 PM
Stream

RONALD ACUNA - UNDER/OVER PLAYER RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406333

OVER
7406334

UNDER
Sep 09 7:20 PM
Stream

KE'BRYAN HAYES - UNDER/OVER PLAYER RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406335

OVER
7406336

UNDER
Sep 09 7:20 PM
Stream

LIOVER PEGUERO - UNDER/OVER PLAYER RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406337

OVER
7406338

UNDER
Sep 09 7:20 PM
Stream

TRAVIS D'ARNAUD - UNDER/OVER PLAYER RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406339

OVER
7406340

UNDER
Sep 09 7:20 PM
Stream

MATT OLSON - UNDER/OVER PLAYER RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406341

OVER
7406342

UNDER
Sep 09 7:20 PM
Stream

MARCELL OZUNA - UNDER/OVER PLAYER RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406343

OVER
7406344

UNDER
Sep 09 7:20 PM
Stream

JI-HWAN BAE - UNDER/OVER PLAYER RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406345

OVER
7406346

UNDER
Sep 09 7:20 PM
Stream

ORLANDO ARCIA - UNDER/OVER PLAYER RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406347

OVER
7406348

UNDER
Sep 09 7:20 PM
Stream

CONNOR JOE - UNDER/OVER PLAYER RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406349

OVER
7406350

UNDER
Sep 09 7:20 PM
Stream

BRYAN REYNOLDS - UNDER/OVER PLAYER RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406351

OVER
7406352

UNDER
Sep 09 7:20 PM
Stream

EZEQUIEL TOVAR - UNDER/OVER PLAYER RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406353

OVER
7406354

UNDER
Sep 09 9:05 PM
Stream

CHARLIE BLACKMON - UNDER/OVER PLAYER RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406355

OVER
7406356

UNDER
Sep 09 9:05 PM
Stream

ELIAS DIAZ - UNDER/OVER PLAYER RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406357

OVER
7406358

UNDER
Sep 09 9:05 PM
Stream

LAMONTE WADE - UNDER/OVER PLAYER RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406359

OVER
7406360

UNDER
Sep 09 9:05 PM
Stream

WILMER FLORES - UNDER/OVER PLAYER RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406361

OVER
7406362

UNDER
Sep 09 9:05 PM
Stream

BRENTON DOYLE - UNDER/OVER PLAYER RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406363

OVER
7406364

UNDER
Sep 09 9:05 PM
Stream

MIKE YASTRZEMSKI - UNDER/OVER PLAYER RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406365

OVER
7406366

UNDER
Sep 09 9:05 PM
Stream

RYAN MCMAHON - UNDER/OVER PLAYER RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406367

OVER
7406368

UNDER
Sep 09 9:05 PM
Stream

NOLAN JONES - UNDER/OVER PLAYER RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406369

OVER
7406370

UNDER
Sep 09 9:05 PM
Stream

THAIRO ESTRADA - UNDER/OVER PLAYER RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406371

OVER
7406372

UNDER
Sep 09 9:05 PM
Stream

BRANDON CRAWFORD - UNDER/OVER PLAYER RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406373

OVER
7406374

UNDER
Sep 09 9:05 PM
Stream

JONATHAN GREGORY J D DAVIS - UNDER/OVER PLAYER RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406375

OVER
7406376

UNDER
Sep 09 9:05 PM
Stream

BRENDAN RODGERS - UNDER/OVER PLAYER RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406377

OVER
7406378

UNDER
Sep 09 9:05 PM
Stream

MITCHELL HANIGER - UNDER/OVER PLAYER RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406379

OVER
7406380

UNDER
Sep 09 9:05 PM
Stream

BLAKE SABOL - UNDER/OVER PLAYER RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406381

OVER
7406382

UNDER
Sep 09 9:05 PM
Stream

ELEHURIS MONTERO - UNDER/OVER PLAYER RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406383

OVER
7406384

UNDER
Sep 09 9:05 PM
Stream

JOC PEDERSON - UNDER/OVER PLAYER RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406385

OVER
7406386

UNDER
Sep 09 9:05 PM
Stream

ANDRES GIMENEZ - UNDER/OVER PLAYER RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406387

OVER
7406388

UNDER
Sep 09 9:07 PM
Stream

MYLES STRAW - UNDER/OVER PLAYER RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406389

OVER
7406390

UNDER
Sep 09 9:07 PM
Stream

JOSE RAMIREZ - UNDER/OVER PLAYER RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406391

OVER
7406392

UNDER
Sep 09 9:07 PM
Stream

MIKE MOUSTAKAS - UNDER/OVER PLAYER RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406393

OVER
7406394

UNDER
Sep 09 9:07 PM
Stream

LOGAN O'HOPPE - UNDER/OVER PLAYER RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406395

OVER
7406396

UNDER
Sep 09 9:07 PM
Stream

STEVEN KWAN - UNDER/OVER PLAYER RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406397

OVER
7406398

UNDER
Sep 09 9:07 PM
Stream

KOLE CALHOUN - UNDER/OVER PLAYER RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406399

OVER
7406400

UNDER
Sep 09 9:07 PM
Stream

GABRIEL ARIAS - UNDER/OVER PLAYER RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406401

OVER
7406402

UNDER
Sep 09 9:07 PM
Stream

RANDAL GRICHUK - UNDER/OVER PLAYER RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406403

OVER
7406404

UNDER
Sep 09 9:07 PM
Stream

NOLAN SCHANUEL - UNDER/OVER PLAYER RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406405

OVER
7406406

UNDER
Sep 09 9:07 PM
Stream

KYREN PARIS - UNDER/OVER PLAYER RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406407

OVER
7406408

UNDER
Sep 09 9:07 PM
Stream

JOSH NAYLOR - UNDER/OVER PLAYER RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406409

OVER
7406410

UNDER
Sep 09 9:07 PM
Stream

BRANDON DRURY - UNDER/OVER PLAYER RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406411

OVER
7406412

UNDER
Sep 09 9:07 PM
Stream

RAMON LAUREANO - UNDER/OVER PLAYER RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406413

OVER
7406414

UNDER
Sep 09 9:07 PM
Stream

MJ MELENDEZ - UNDER/OVER PLAYER RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406415

OVER
7406416

UNDER
Sep 09 3:07 PM
Stream

GEORGE SPRINGER - UNDER/OVER PLAYER RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406417

OVER
7406418

UNDER
Sep 09 3:07 PM
Stream

MAIKEL GARCIA - UNDER/OVER PLAYER RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406419

OVER
7406420

UNDER
Sep 09 3:07 PM
Stream

SALVADOR PEREZ - UNDER/OVER PLAYER RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406421

OVER
7406422

UNDER
Sep 09 3:07 PM
Stream

EDWARD OLIVARES - UNDER/OVER PLAYER RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406423

OVER
7406424

UNDER
Sep 09 3:07 PM
Stream

WHIT MERRIFIELD - UNDER/OVER PLAYER RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406425

OVER
7406426

UNDER
Sep 09 3:07 PM
Stream

MICHAEL MASSEY - UNDER/OVER PLAYER RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406427

OVER
7406428

UNDER
Sep 09 3:07 PM
Stream

BOBBY WITT JR. - UNDER/OVER PLAYER RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406429

OVER
7406430

UNDER
Sep 09 3:07 PM
Stream

DREW WATERS - UNDER/OVER PLAYER RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406431

OVER
7406432

UNDER
Sep 09 3:07 PM
Stream

NICK LOFTIN - UNDER/OVER PLAYER RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406433

OVER
7406434

UNDER
Sep 09 3:07 PM
Stream

VLADIMIR GUERRERO JR. - UNDER/OVER PLAYER RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406435

OVER
7406436

UNDER
Sep 09 3:07 PM
Stream

KEVIN KIERMAIER - UNDER/OVER PLAYER RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406437

OVER
7406438

UNDER
Sep 09 3:07 PM
Stream

ALEJANDRO KIRK - UNDER/OVER PLAYER RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406439

OVER
7406440

UNDER
Sep 09 3:07 PM
Stream

NELSON VELÁZQUEZ - UNDER/OVER PLAYER RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406441

OVER
7406442

UNDER
Sep 09 3:07 PM
Stream

CAVAN BIGGIO - UNDER/OVER PLAYER RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406443

OVER
7406444

UNDER
Sep 09 3:07 PM
Stream

BO BICHETTE - UNDER/OVER PLAYER RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406445

OVER
7406446

UNDER
Sep 09 3:07 PM
Stream

DAULTON VARSHO - UNDER/OVER PLAYER RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7406447

OVER
7406448

UNDER
Sep 09 3:07 PM
Stream

MLB - PLAYER TOTAL HOME RUNS
SAL FRELICK - UNDER/OVER PLAYER HOME RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407003

OVER
7407004

UNDER
Sep 09 2:05 PM
Stream

BRICE TURANG - UNDER/OVER PLAYER HOME RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407005

OVER
7407006

UNDER
Sep 09 2:05 PM
Stream

DAVID JOHN LEMAHIEU - UNDER/OVER PLAYER HOME RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407007

OVER
7407008

UNDER
Sep 09 2:05 PM
Stream

GLEYBER TORRES - UNDER/OVER PLAYER HOME RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407009

OVER
7407010

UNDER
Sep 09 2:05 PM
Stream

JASSON DOMINGUEZ - UNDER/OVER PLAYER HOME RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407011

OVER
7407012

UNDER
Sep 09 2:05 PM
Stream

OSWALD PERAZA - UNDER/OVER PLAYER HOME RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407013

OVER
7407014

UNDER
Sep 09 2:05 PM
Stream

TYRONE TAYLOR - UNDER/OVER PLAYER HOME RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407015

OVER
7407016

UNDER
Sep 09 2:05 PM
Stream

ANTHONY VOLPE - UNDER/OVER PLAYER HOME RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407017

OVER
7407018

UNDER
Sep 09 2:05 PM
Stream

ANDRUW MONASTERIO - UNDER/OVER PLAYER HOME RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407019

OVER
7407020

UNDER
Sep 09 2:05 PM
Stream

WILLIAM CONTRERAS - UNDER/OVER PLAYER HOME RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407021

OVER
7407022

UNDER
Sep 09 2:05 PM
Stream

KYLE HIGASHIOKA - UNDER/OVER PLAYER HOME RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407023

OVER
7407024

UNDER
Sep 09 2:05 PM
Stream

CHRISTIAN YELICH - UNDER/OVER PLAYER HOME RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407025

OVER
7407026

UNDER
Sep 09 2:05 PM
Stream

GIANCARLO STANTON - UNDER/OVER PLAYER HOME RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407027

OVER
7407028

UNDER
Sep 09 2:05 PM
Stream

AUSTIN WELLS - UNDER/OVER PLAYER HOME RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407029

OVER
7407030

UNDER
Sep 09 2:05 PM
Stream

AARON JUDGE - UNDER/OVER PLAYER HOME RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407031

OVER
7407032

UNDER
Sep 09 2:05 PM
Stream

WILLY ADAMES - UNDER/OVER PLAYER HOME RUNS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407033

OVER
7407034

UNDER
Sep 09 2:05 PM
Stream

RAFAEL ORTEGA - UNDER/OVER PLAYER HOME RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407035

OVER
7407036

UNDER
Sep 09 2:10 PM
Stream

MARK VIENTOS - UNDER/OVER PLAYER HOME RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407037

OVER
7407038

UNDER
Sep 09 2:10 PM
Stream

RONNY MAURICIO - UNDER/OVER PLAYER HOME RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407039

OVER
7407040

UNDER
Sep 09 2:10 PM
Stream

RYAN JEFFERS - UNDER/OVER PLAYER HOME RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407041

OVER
7407042

UNDER
Sep 09 2:10 PM
Stream

PETER ALONSO - UNDER/OVER PLAYER HOME RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407043

OVER
7407044

UNDER
Sep 09 2:10 PM
Stream

BRANDON NIMMO - UNDER/OVER PLAYER HOME RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407045

OVER
7407046

UNDER
Sep 09 2:10 PM
Stream

BRETT BATY - UNDER/OVER PLAYER HOME RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407047

OVER
7407048

UNDER
Sep 09 2:10 PM
Stream

KYLE FARMER - UNDER/OVER PLAYER HOME RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407049

OVER
7407050

UNDER
Sep 09 2:10 PM
Stream

MATT WALLNER - UNDER/OVER PLAYER HOME RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407051

OVER
7407052

UNDER
Sep 09 2:10 PM
Stream

WILLI CASTRO - UNDER/OVER PLAYER HOME RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407053

OVER
7407054

UNDER
Sep 09 2:10 PM
Stream

FRANCISCO LINDOR - UNDER/OVER PLAYER HOME RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407055

OVER
7407056

UNDER
Sep 09 2:10 PM
Stream

CARLOS CORREA - UNDER/OVER PLAYER HOME RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407057

OVER
7407058

UNDER
Sep 09 2:10 PM
Stream

JORDAN LUPLOW - UNDER/OVER PLAYER HOME RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407059

OVER
7407060

UNDER
Sep 09 2:10 PM
Stream

ROYCE LEWIS - UNDER/OVER PLAYER HOME RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407061

OVER
7407062

UNDER
Sep 09 2:10 PM
Stream

DONOVAN SOLANO - UNDER/OVER PLAYER HOME RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407063

OVER
7407064

UNDER
Sep 09 2:10 PM
Stream

JEFF MCNEIL - UNDER/OVER PLAYER HOME RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407065

OVER
7407066

UNDER
Sep 09 2:10 PM
Stream

OMAR NARVAEZ - UNDER/OVER PLAYER HOME RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407067

OVER
7407068

UNDER
Sep 09 2:10 PM
Stream

JORGE POLANCO - UNDER/OVER PLAYER HOME RUNS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407069

OVER
7407070

UNDER
Sep 09 2:10 PM
Stream

GABRIEL MORENO - UNDER/OVER PLAYER HOME RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407071

OVER
7407072

UNDER
Sep 09 2:20 PM
Stream

TOMMY PHAM - UNDER/OVER PLAYER HOME RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407073

OVER
7407074

UNDER
Sep 09 2:20 PM
Stream

CORBIN CARROLL - UNDER/OVER PLAYER HOME RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407075

OVER
7407076

UNDER
Sep 09 2:20 PM
Stream

CODY BELLINGER - UNDER/OVER PLAYER HOME RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407077

OVER
7407078

UNDER
Sep 09 2:20 PM
Stream

EMMANUEL RIVERA - UNDER/OVER PLAYER HOME RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407079

OVER
7407080

UNDER
Sep 09 2:20 PM
Stream

NICO HOERNER - UNDER/OVER PLAYER HOME RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407081

OVER
7407082

UNDER
Sep 09 2:20 PM
Stream

GERALDO PERDOMO - UNDER/OVER PLAYER HOME RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407083

OVER
7407084

UNDER
Sep 09 2:20 PM
Stream

JEIMER CANDELARIO - UNDER/OVER PLAYER HOME RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407085

OVER
7407086

UNDER
Sep 09 2:20 PM
Stream

CHRISTIAN WALKER - UNDER/OVER PLAYER HOME RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407087

OVER
7407088

UNDER
Sep 09 2:20 PM
Stream

EVAN LONGORIA - UNDER/OVER PLAYER HOME RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407089

OVER
7407090

UNDER
Sep 09 2:20 PM
Stream

SEIYA SUZUKI - UNDER/OVER PLAYER HOME RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407091

OVER
7407092

UNDER
Sep 09 2:20 PM
Stream

MIKE TAUCHMAN - UNDER/OVER PLAYER HOME RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407093

OVER
7407094

UNDER
Sep 09 2:20 PM
Stream

DANSBY SWANSON - UNDER/OVER PLAYER HOME RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407095

OVER
7407096

UNDER
Sep 09 2:20 PM
Stream

YAN GOMES - UNDER/OVER PLAYER HOME RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407097

OVER
7407098

UNDER
Sep 09 2:20 PM
Stream

KETEL MARTE - UNDER/OVER PLAYER HOME RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407099

OVER
7407100

UNDER
Sep 09 2:20 PM
Stream

LOURDES GURRIEL - UNDER/OVER PLAYER HOME RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407101

OVER
7407102

UNDER
Sep 09 2:20 PM
Stream

IAN HAPP - UNDER/OVER PLAYER HOME RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407103

OVER
7407104

UNDER
Sep 09 2:20 PM
Stream

NICK MADRIGAL - UNDER/OVER PLAYER HOME RUNS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407105

OVER
7407106

UNDER
Sep 09 2:20 PM
Stream

JASON HEYWARD - UNDER/OVER PLAYER HOME RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407107

OVER
7407108

UNDER
Sep 09 4:05 PM
Stream

JOEY MENESES - UNDER/OVER PLAYER HOME RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407109

OVER
7407110

UNDER
Sep 09 4:05 PM
Stream

ALEX CALL - UNDER/OVER PLAYER HOME RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407111

OVER
7407112

UNDER
Sep 09 4:05 PM
Stream

JAMES OUTMAN - UNDER/OVER PLAYER HOME RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407113

OVER
7407114

UNDER
Sep 09 4:05 PM
Stream

KEIBERT RUIZ - UNDER/OVER PLAYER HOME RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407115

OVER
7407116

UNDER
Sep 09 4:05 PM
Stream

MAX MUNCY - UNDER/OVER PLAYER HOME RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407117

OVER
7407118

UNDER
Sep 09 4:05 PM
Stream

JACOB YOUNG - UNDER/OVER PLAYER HOME RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407119

OVER
7407120

UNDER
Sep 09 4:05 PM
Stream

J.D. MARTINEZ - UNDER/OVER PLAYER HOME RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407121

OVER
7407122

UNDER
Sep 09 4:05 PM
Stream

DOMINIC SMITH - UNDER/OVER PLAYER HOME RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407123

OVER
7407124

UNDER
Sep 09 4:05 PM
Stream

MIGUEL ROJAS - UNDER/OVER PLAYER HOME RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407125

OVER
7407126

UNDER
Sep 09 4:05 PM
Stream

JAKE ALU - UNDER/OVER PLAYER HOME RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407127

OVER
7407128

UNDER
Sep 09 4:05 PM
Stream

ENRIQUE HERNANDEZ - UNDER/OVER PLAYER HOME RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407129

OVER
7407130

UNDER
Sep 09 4:05 PM
Stream

LANE THOMAS - UNDER/OVER PLAYER HOME RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407131

OVER
7407132

UNDER
Sep 09 4:05 PM
Stream

CARTER KIEBOOM - UNDER/OVER PLAYER HOME RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407133

OVER
7407134

UNDER
Sep 09 4:05 PM
Stream

FREDDIE FREEMAN - UNDER/OVER PLAYER HOME RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407135

OVER
7407136

UNDER
Sep 09 4:05 PM
Stream

CJ ABRAMS - UNDER/OVER PLAYER HOME RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407137

OVER
7407138

UNDER
Sep 09 4:05 PM
Stream

WILL SMITH - UNDER/OVER PLAYER HOME RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407139

OVER
7407140

UNDER
Sep 09 4:05 PM
Stream

DAVID PERALTA - UNDER/OVER PLAYER HOME RUNS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407141

OVER
7407142

UNDER
Sep 09 4:05 PM
Stream

JULIO RODRIGUEZ - UNDER/OVER PLAYER HOME RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407143

OVER
7407144

UNDER
Sep 09 4:05 PM
Stream

RANDY AROZARENA - UNDER/OVER PLAYER HOME RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407145

OVER
7407146

UNDER
Sep 09 4:05 PM
Stream

CHRISTIAN BETHANCOURT - UNDER/OVER PLAYER HOME RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407147

OVER
7407148

UNDER
Sep 09 4:05 PM
Stream

TAYLOR WALLS - UNDER/OVER PLAYER HOME RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407149

OVER
7407150

UNDER
Sep 09 4:05 PM
Stream

DOMINIC CANZONE - UNDER/OVER PLAYER HOME RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407151

OVER
7407152

UNDER
Sep 09 4:05 PM
Stream

TEOSCAR HERNÁNDEZ - UNDER/OVER PLAYER HOME RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407153

OVER
7407154

UNDER
Sep 09 4:05 PM
Stream

BRANDON LOWE - UNDER/OVER PLAYER HOME RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407155

OVER
7407156

UNDER
Sep 09 4:05 PM
Stream

EUGENIO SUAREZ - UNDER/OVER PLAYER HOME RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407157

OVER
7407158

UNDER
Sep 09 4:05 PM
Stream

TY FRANCE - UNDER/OVER PLAYER HOME RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407159

OVER
7407160

UNDER
Sep 09 4:05 PM
Stream

J.P. CRAWFORD - UNDER/OVER PLAYER HOME RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407161

OVER
7407162

UNDER
Sep 09 4:05 PM
Stream

YANDY DIAZ - UNDER/OVER PLAYER HOME RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407163

OVER
7407164

UNDER
Sep 09 4:05 PM
Stream

JOSHUA ROJAS - UNDER/OVER PLAYER HOME RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407165

OVER
7407166

UNDER
Sep 09 4:05 PM
Stream

MIKE FORD - UNDER/OVER PLAYER HOME RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407167

OVER
7407168

UNDER
Sep 09 4:05 PM
Stream

CAL RALEIGH - UNDER/OVER PLAYER HOME RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407169

OVER
7407170

UNDER
Sep 09 4:05 PM
Stream

JOSE SIRI - UNDER/OVER PLAYER HOME RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407171

OVER
7407172

UNDER
Sep 09 4:05 PM
Stream

ISAAC PAREDES - UNDER/OVER PLAYER HOME RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407173

OVER
7407174

UNDER
Sep 09 4:05 PM
Stream

LUKE RALEY - UNDER/OVER PLAYER HOME RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407175

OVER
7407176

UNDER
Sep 09 4:05 PM
Stream

JOSH LOWE - UNDER/OVER PLAYER HOME RUNS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407177

OVER
7407178

UNDER
Sep 09 4:05 PM
Stream

MASATAKA YOSHIDA - UNDER/OVER PLAYER HOME RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407179

OVER
7407180

UNDER
Sep 09 4:10 PM
Stream

ALEX VERDUGO - UNDER/OVER PLAYER HOME RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407181

OVER
7407182

UNDER
Sep 09 4:10 PM
Stream

RAMON URIAS - UNDER/OVER PLAYER HOME RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407183

OVER
7407184

UNDER
Sep 09 4:10 PM
Stream

JORGE MATEO - UNDER/OVER PLAYER HOME RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407185

OVER
7407186

UNDER
Sep 09 4:10 PM
Stream

RAFAEL DEVERS - UNDER/OVER PLAYER HOME RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407187

OVER
7407188

UNDER
Sep 09 4:10 PM
Stream

ADAM DUVALL - UNDER/OVER PLAYER HOME RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407189

OVER
7407190

UNDER
Sep 09 4:10 PM
Stream

AUSTIN HAYS - UNDER/OVER PLAYER HOME RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407191

OVER
7407192

UNDER
Sep 09 4:10 PM
Stream

ADLEY RUTSCHMAN - UNDER/OVER PLAYER HOME RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407193

OVER
7407194

UNDER
Sep 09 4:10 PM
Stream

CONNOR WONG - UNDER/OVER PLAYER HOME RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407195

OVER
7407196

UNDER
Sep 09 4:10 PM
Stream

JAMES MCCANN - UNDER/OVER PLAYER HOME RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407197

OVER
7407198

UNDER
Sep 09 4:10 PM
Stream

ANTHONY SANTANDER - UNDER/OVER PLAYER HOME RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407199

OVER
7407200

UNDER
Sep 09 4:10 PM
Stream

TREVOR STORY - UNDER/OVER PLAYER HOME RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407201

OVER
7407202

UNDER
Sep 09 4:10 PM
Stream

AARON HICKS - UNDER/OVER PLAYER HOME RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407203

OVER
7407204

UNDER
Sep 09 4:10 PM
Stream

TRISTON CASAS - UNDER/OVER PLAYER HOME RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407205

OVER
7407206

UNDER
Sep 09 4:10 PM
Stream

RYAN MOUNTCASTLE - UNDER/OVER PLAYER HOME RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407207

OVER
7407208

UNDER
Sep 09 4:10 PM
Stream

JUSTIN TURNER - UNDER/OVER PLAYER HOME RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407209

OVER
7407210

UNDER
Sep 09 4:10 PM
Stream

GUNNAR HENDERSON - UNDER/OVER PLAYER HOME RUNS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407211

OVER
7407212

UNDER
Sep 09 4:10 PM
Stream

JAKE CAVE - UNDER/OVER PLAYER HOME RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407213

OVER
7407214

UNDER
Sep 09 6:05 PM
Stream

BRYCE HARPER - UNDER/OVER PLAYER HOME RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407215

OVER
7407216

UNDER
Sep 09 6:05 PM
Stream

LUIS ARRAEZ - UNDER/OVER PLAYER HOME RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407217

OVER
7407218

UNDER
Sep 09 6:05 PM
Stream

JAZZ CHISHOLM - UNDER/OVER PLAYER HOME RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407219

OVER
7407220

UNDER
Sep 09 6:05 PM
Stream

BRANDON MARSH - UNDER/OVER PLAYER HOME RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407221

OVER
7407222

UNDER
Sep 09 6:05 PM
Stream

JESUS SANCHEZ - UNDER/OVER PLAYER HOME RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407223

OVER
7407224

UNDER
Sep 09 6:05 PM
Stream

JACOB MICHAEL BURGER - UNDER/OVER PLAYER HOME RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407225

OVER
7407226

UNDER
Sep 09 6:05 PM
Stream

JOSHUA EVAN BELL - UNDER/OVER PLAYER HOME RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407227

OVER
7407228

UNDER
Sep 09 6:05 PM
Stream

KYLE SCHWARBER - UNDER/OVER PLAYER HOME RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407229

OVER
7407230

UNDER
Sep 09 6:05 PM
Stream

BRYAN DE LA CRUZ - UNDER/OVER PLAYER HOME RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407231

OVER
7407232

UNDER
Sep 09 6:05 PM
Stream

NICK FORTES - UNDER/OVER PLAYER HOME RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407233

OVER
7407234

UNDER
Sep 09 6:05 PM
Stream

ALEC BOHM - UNDER/OVER PLAYER HOME RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407235

OVER
7407236

UNDER
Sep 09 6:05 PM
Stream

BRYSON STOTT - UNDER/OVER PLAYER HOME RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407237

OVER
7407238

UNDER
Sep 09 6:05 PM
Stream

NICK CASTELLANOS - UNDER/OVER PLAYER HOME RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407239

OVER
7407240

UNDER
Sep 09 6:05 PM
Stream

TREA TURNER - UNDER/OVER PLAYER HOME RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407241

OVER
7407242

UNDER
Sep 09 6:05 PM
Stream

J.T. REALMUTO - UNDER/OVER PLAYER HOME RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407243

OVER
7407244

UNDER
Sep 09 6:05 PM
Stream

JOEY WENDLE - UNDER/OVER PLAYER HOME RUNS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407245

OVER
7407246

UNDER
Sep 09 6:05 PM
Stream

LARS NOOTBAAR - UNDER/OVER PLAYER HOME RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407247

OVER
7407248

UNDER
Sep 09 6:40 PM
Stream

NOELVI MARTE - UNDER/OVER PLAYER HOME RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407249

OVER
7407250

UNDER
Sep 09 6:40 PM
Stream

WILLSON CONTRERAS - UNDER/OVER PLAYER HOME RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407251

OVER
7407252

UNDER
Sep 09 6:40 PM
Stream

HUNTER RENFROE - UNDER/OVER PLAYER HOME RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407253

OVER
7407254

UNDER
Sep 09 6:40 PM
Stream

STUART FAIRCHILD - UNDER/OVER PLAYER HOME RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407255

OVER
7407256

UNDER
Sep 09 6:40 PM
Stream

TYLER O'NEILL - UNDER/OVER PLAYER HOME RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407257

OVER
7407258

UNDER
Sep 09 6:40 PM
Stream

HARRISON BADER - UNDER/OVER PLAYER HOME RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407259

OVER
7407260

UNDER
Sep 09 6:40 PM
Stream

TYLER STEPHENSON - UNDER/OVER PLAYER HOME RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407261

OVER
7407262

UNDER
Sep 09 6:40 PM
Stream

MASYN WINN - UNDER/OVER PLAYER HOME RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407263

OVER
7407264

UNDER
Sep 09 6:40 PM
Stream

NOLAN GORMAN - UNDER/OVER PLAYER HOME RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407265

OVER
7407266

UNDER
Sep 09 6:40 PM
Stream

NOLAN ARENADO - UNDER/OVER PLAYER HOME RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407267

OVER
7407268

UNDER
Sep 09 6:40 PM
Stream

JORDAN WALKER - UNDER/OVER PLAYER HOME RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407269

OVER
7407270

UNDER
Sep 09 6:40 PM
Stream

PAUL GOLDSCHMIDT - UNDER/OVER PLAYER HOME RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407271

OVER
7407272

UNDER
Sep 09 6:40 PM
Stream

TOMMY EDMAN - UNDER/OVER PLAYER HOME RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407273

OVER
7407274

UNDER
Sep 09 6:40 PM
Stream

ELLY DE LA CRUZ - UNDER/OVER PLAYER HOME RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407275

OVER
7407276

UNDER
Sep 09 6:40 PM
Stream

SPENCER STEER - UNDER/OVER PLAYER HOME RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407277

OVER
7407278

UNDER
Sep 09 6:40 PM
Stream

NICK SENZEL - UNDER/OVER PLAYER HOME RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407279

OVER
7407280

UNDER
Sep 09 6:40 PM
Stream

CHRISTIAN ENCARNACION-STRAND - UNDER/OVER PLAYER HOME RUNS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407281

OVER
7407282

UNDER
Sep 09 6:40 PM
Stream

HA-SEONG KIM - UNDER/OVER PLAYER HOME RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407283

OVER
7407284

UNDER
Sep 09 7:10 PM
Stream

JOSE ABREU - UNDER/OVER PLAYER HOME RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407285

OVER
7407286

UNDER
Sep 09 7:10 PM
Stream

JOSE ALTUVE - UNDER/OVER PLAYER HOME RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407287

OVER
7407288

UNDER
Sep 09 7:10 PM
Stream

YORDAN ALVAREZ - UNDER/OVER PLAYER HOME RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407289

OVER
7407290

UNDER
Sep 09 7:10 PM
Stream

JEREMY PENA - UNDER/OVER PLAYER HOME RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407291

OVER
7407292

UNDER
Sep 09 7:10 PM
Stream

KYLE TUCKER - UNDER/OVER PLAYER HOME RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407293

OVER
7407294

UNDER
Sep 09 7:10 PM
Stream

TRENT GRISHAM - UNDER/OVER PLAYER HOME RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407295

OVER
7407296

UNDER
Sep 09 7:10 PM
Stream

JUAN SOTO - UNDER/OVER PLAYER HOME RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407297

OVER
7407298

UNDER
Sep 09 7:10 PM
Stream

LUIS CAMPUSANO - UNDER/OVER PLAYER HOME RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407299

OVER
7407300

UNDER
Sep 09 7:10 PM
Stream

FERNANDO TATIS JR. - UNDER/OVER PLAYER HOME RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407301

OVER
7407302

UNDER
Sep 09 7:10 PM
Stream

MANNY MACHADO - UNDER/OVER PLAYER HOME RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407303

OVER
7407304

UNDER
Sep 09 7:10 PM
Stream

MAURICIO DUBÓN - UNDER/OVER PLAYER HOME RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407305

OVER
7407306

UNDER
Sep 09 7:10 PM
Stream

GARRETT COOPER - UNDER/OVER PLAYER HOME RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407307

OVER
7407308

UNDER
Sep 09 7:10 PM
Stream

ALEX BREGMAN - UNDER/OVER PLAYER HOME RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407309

OVER
7407310

UNDER
Sep 09 7:10 PM
Stream

MARTIN MALDONADO - UNDER/OVER PLAYER HOME RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407311

OVER
7407312

UNDER
Sep 09 7:10 PM
Stream

XANDER BOGAERTS - UNDER/OVER PLAYER HOME RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407313

OVER
7407314

UNDER
Sep 09 7:10 PM
Stream

MICHAEL BRANTLEY - UNDER/OVER PLAYER HOME RUNS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407315

OVER
7407316

UNDER
Sep 09 7:10 PM
Stream

JARED TRIOLO - UNDER/OVER PLAYER HOME RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407317

OVER
7407318

UNDER
Sep 09 7:20 PM
Stream

RONALD ACUNA - UNDER/OVER PLAYER HOME RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407319

OVER
7407320

UNDER
Sep 09 7:20 PM
Stream

EDDIE ROSARIO - UNDER/OVER PLAYER HOME RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407321

OVER
7407322

UNDER
Sep 09 7:20 PM
Stream

KE'BRYAN HAYES - UNDER/OVER PLAYER HOME RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407323

OVER
7407324

UNDER
Sep 09 7:20 PM
Stream

ENDY RODRIGUEZ - UNDER/OVER PLAYER HOME RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407325

OVER
7407326

UNDER
Sep 09 7:20 PM
Stream

ORLANDO ARCIA - UNDER/OVER PLAYER HOME RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407327

OVER
7407328

UNDER
Sep 09 7:20 PM
Stream

MICHAEL HARRIS - UNDER/OVER PLAYER HOME RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407329

OVER
7407330

UNDER
Sep 09 7:20 PM
Stream

MATT OLSON - UNDER/OVER PLAYER HOME RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407331

OVER
7407332

UNDER
Sep 09 7:20 PM
Stream

ALIKA WILLIAMS - UNDER/OVER PLAYER HOME RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407333

OVER
7407334

UNDER
Sep 09 7:20 PM
Stream

LIOVER PEGUERO - UNDER/OVER PLAYER HOME RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407335

OVER
7407336

UNDER
Sep 09 7:20 PM
Stream

TRAVIS D'ARNAUD - UNDER/OVER PLAYER HOME RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407337

OVER
7407338

UNDER
Sep 09 7:20 PM
Stream

AUSTIN RILEY - UNDER/OVER PLAYER HOME RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407339

OVER
7407340

UNDER
Sep 09 7:20 PM
Stream

MIGUEL ANDÚJAR - UNDER/OVER PLAYER HOME RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407341

OVER
7407342

UNDER
Sep 09 7:20 PM
Stream

BRYAN REYNOLDS - UNDER/OVER PLAYER HOME RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407343

OVER
7407344

UNDER
Sep 09 7:20 PM
Stream

OZZIE ALBIES - UNDER/OVER PLAYER HOME RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407345

OVER
7407346

UNDER
Sep 09 7:20 PM
Stream

JI-HWAN BAE - UNDER/OVER PLAYER HOME RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407347

OVER
7407348

UNDER
Sep 09 7:20 PM
Stream

CONNOR JOE - UNDER/OVER PLAYER HOME RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407349

OVER
7407350

UNDER
Sep 09 7:20 PM
Stream

MARCELL OZUNA - UNDER/OVER PLAYER HOME RUNS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407351

OVER
7407352

UNDER
Sep 09 7:20 PM
Stream

EZEQUIEL TOVAR - UNDER/OVER PLAYER HOME RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407353

OVER
7407354

UNDER
Sep 09 9:05 PM
Stream

MITCHELL HANIGER - UNDER/OVER PLAYER HOME RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407355

OVER
7407356

UNDER
Sep 09 9:05 PM
Stream

MIKE YASTRZEMSKI - UNDER/OVER PLAYER HOME RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407357

OVER
7407358

UNDER
Sep 09 9:05 PM
Stream

BLAKE SABOL - UNDER/OVER PLAYER HOME RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407359

OVER
7407360

UNDER
Sep 09 9:05 PM
Stream

LAMONTE WADE - UNDER/OVER PLAYER HOME RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407361

OVER
7407362

UNDER
Sep 09 9:05 PM
Stream

RYAN MCMAHON - UNDER/OVER PLAYER HOME RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407363

OVER
7407364

UNDER
Sep 09 9:05 PM
Stream

NOLAN JONES - UNDER/OVER PLAYER HOME RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407365

OVER
7407366

UNDER
Sep 09 9:05 PM
Stream

BRANDON CRAWFORD - UNDER/OVER PLAYER HOME RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407367

OVER
7407368

UNDER
Sep 09 9:05 PM
Stream

BRENDAN RODGERS - UNDER/OVER PLAYER HOME RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407369

OVER
7407370

UNDER
Sep 09 9:05 PM
Stream

THAIRO ESTRADA - UNDER/OVER PLAYER HOME RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407371

OVER
7407372

UNDER
Sep 09 9:05 PM
Stream

WILMER FLORES - UNDER/OVER PLAYER HOME RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407373

OVER
7407374

UNDER
Sep 09 9:05 PM
Stream

BRENTON DOYLE - UNDER/OVER PLAYER HOME RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407375

OVER
7407376

UNDER
Sep 09 9:05 PM
Stream

ELIAS DIAZ - UNDER/OVER PLAYER HOME RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407377

OVER
7407378

UNDER
Sep 09 9:05 PM
Stream

JONATHAN GREGORY J D DAVIS - UNDER/OVER PLAYER HOME RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407379

OVER
7407380

UNDER
Sep 09 9:05 PM
Stream

ELEHURIS MONTERO - UNDER/OVER PLAYER HOME RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407381

OVER
7407382

UNDER
Sep 09 9:05 PM
Stream

CHARLIE BLACKMON - UNDER/OVER PLAYER HOME RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407383

OVER
7407384

UNDER
Sep 09 9:05 PM
Stream

JOC PEDERSON - UNDER/OVER PLAYER HOME RUNS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407385

OVER
7407386

UNDER
Sep 09 9:05 PM
Stream

GABRIEL ARIAS - UNDER/OVER PLAYER HOME RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407387

OVER
7407388

UNDER
Sep 09 9:07 PM
Stream

RAMON LAUREANO - UNDER/OVER PLAYER HOME RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407389

OVER
7407390

UNDER
Sep 09 9:07 PM
Stream

MIKE MOUSTAKAS - UNDER/OVER PLAYER HOME RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407391

OVER
7407392

UNDER
Sep 09 9:07 PM
Stream

JOSH NAYLOR - UNDER/OVER PLAYER HOME RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407393

OVER
7407394

UNDER
Sep 09 9:07 PM
Stream

LOGAN O'HOPPE - UNDER/OVER PLAYER HOME RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407395

OVER
7407396

UNDER
Sep 09 9:07 PM
Stream

MYLES STRAW - UNDER/OVER PLAYER HOME RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407397

OVER
7407398

UNDER
Sep 09 9:07 PM
Stream

RANDAL GRICHUK - UNDER/OVER PLAYER HOME RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407399

OVER
7407400

UNDER
Sep 09 9:07 PM
Stream

ANDRES GIMENEZ - UNDER/OVER PLAYER HOME RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407401

OVER
7407402

UNDER
Sep 09 9:07 PM
Stream

JOSE RAMIREZ - UNDER/OVER PLAYER HOME RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407403

OVER
7407404

UNDER
Sep 09 9:07 PM
Stream

KOLE CALHOUN - UNDER/OVER PLAYER HOME RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407405

OVER
7407406

UNDER
Sep 09 9:07 PM
Stream

BRANDON DRURY - UNDER/OVER PLAYER HOME RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407407

OVER
7407408

UNDER
Sep 09 9:07 PM
Stream

NOLAN SCHANUEL - UNDER/OVER PLAYER HOME RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407409

OVER
7407410

UNDER
Sep 09 9:07 PM
Stream

STEVEN KWAN - UNDER/OVER PLAYER HOME RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407411

OVER
7407412

UNDER
Sep 09 9:07 PM
Stream

KYREN PARIS - UNDER/OVER PLAYER HOME RUNS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407413

OVER
7407414

UNDER
Sep 09 9:07 PM
Stream

MJ MELENDEZ - UNDER/OVER PLAYER HOME RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407415

OVER
7407416

UNDER
Sep 09 3:07 PM
Stream

BOBBY WITT JR. - UNDER/OVER PLAYER HOME RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407417

OVER
7407418

UNDER
Sep 09 3:07 PM
Stream

CAVAN BIGGIO - UNDER/OVER PLAYER HOME RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407419

OVER
7407420

UNDER
Sep 09 3:07 PM
Stream

MICHAEL MASSEY - UNDER/OVER PLAYER HOME RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407421

OVER
7407422

UNDER
Sep 09 3:07 PM
Stream

BO BICHETTE - UNDER/OVER PLAYER HOME RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407423

OVER
7407424

UNDER
Sep 09 3:07 PM
Stream

VLADIMIR GUERRERO JR. - UNDER/OVER PLAYER HOME RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407425

OVER
7407426

UNDER
Sep 09 3:07 PM
Stream

NICK LOFTIN - UNDER/OVER PLAYER HOME RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407427

OVER
7407428

UNDER
Sep 09 3:07 PM
Stream

WHIT MERRIFIELD - UNDER/OVER PLAYER HOME RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407429

OVER
7407430

UNDER
Sep 09 3:07 PM
Stream

EDWARD OLIVARES - UNDER/OVER PLAYER HOME RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407431

OVER
7407432

UNDER
Sep 09 3:07 PM
Stream

MAIKEL GARCIA - UNDER/OVER PLAYER HOME RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407433

OVER
7407434

UNDER
Sep 09 3:07 PM
Stream

NELSON VELÁZQUEZ - UNDER/OVER PLAYER HOME RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407435

OVER
7407436

UNDER
Sep 09 3:07 PM
Stream

KEVIN KIERMAIER - UNDER/OVER PLAYER HOME RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407437

OVER
7407438

UNDER
Sep 09 3:07 PM
Stream

DAULTON VARSHO - UNDER/OVER PLAYER HOME RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407439

OVER
7407440

UNDER
Sep 09 3:07 PM
Stream

ALEJANDRO KIRK - UNDER/OVER PLAYER HOME RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407441

OVER
7407442

UNDER
Sep 09 3:07 PM
Stream

DREW WATERS - UNDER/OVER PLAYER HOME RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407443

OVER
7407444

UNDER
Sep 09 3:07 PM
Stream

SALVADOR PEREZ - UNDER/OVER PLAYER HOME RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407445

OVER
7407446

UNDER
Sep 09 3:07 PM
Stream

GEORGE SPRINGER - UNDER/OVER PLAYER HOME RUNS (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7407447

OVER
7407448

UNDER
Sep 09 3:07 PM
Stream

MLB - PITCHER PROPS (MUST START FOR ACTION)
MICHAEL KING - UNDER/OVER PITCHER OUTS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401003

OVER
7401004

UNDER
Sep 09 2:05 PM
Stream

WADE MILEY - UNDER/OVER PITCHER OUTS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401005

OVER
7401006

UNDER
Sep 09 2:05 PM
Stream

WADE MILEY - UNDER/OVER PITCHER STRIKEOUTS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401007

OVER
7401008

UNDER
Sep 09 2:05 PM
Stream

MICHAEL KING - UNDER/OVER PITCHER STRIKEOUTS (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401009

OVER
7401010

UNDER
Sep 09 2:05 PM
Stream

MICHAEL KING - UNDER/OVER PITCHER HITS ALLOWED (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401011

OVER
7401012

UNDER
Sep 09 2:05 PM
Stream

WADE MILEY - UNDER/OVER PITCHER HITS ALLOWED (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401013

OVER
7401014

UNDER
Sep 09 2:05 PM
Stream

MICHAEL KING - UNDER/OVER PITCHER RUNS EARNED (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401015

OVER
7401016

UNDER
Sep 09 2:05 PM
Stream

WADE MILEY - UNDER/OVER PITCHER RUNS EARNED (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401017

OVER
7401018

UNDER
Sep 09 2:05 PM
Stream

WADE MILEY - PITCHER TO RECORD THE WIN (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401019

NO
7401020

YES
Sep 09 2:05 PM
Stream

MICHAEL KING - PITCHER TO RECORD THE WIN (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401021

NO
7401022

YES
Sep 09 2:05 PM
Stream

KENTA MAEDA - UNDER/OVER PITCHER OUTS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401023

OVER
7401024

UNDER
Sep 09 2:10 PM
Stream

DAVID PETERSON - UNDER/OVER PITCHER OUTS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401025

OVER
7401026

UNDER
Sep 09 2:10 PM
Stream

KENTA MAEDA - UNDER/OVER PITCHER STRIKEOUTS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401027

OVER
7401028

UNDER
Sep 09 2:10 PM
Stream

DAVID PETERSON - UNDER/OVER PITCHER STRIKEOUTS (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401029

OVER
7401030

UNDER
Sep 09 2:10 PM
Stream

DAVID PETERSON - UNDER/OVER PITCHER HITS ALLOWED (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401031

OVER
7401032

UNDER
Sep 09 2:10 PM
Stream

KENTA MAEDA - UNDER/OVER PITCHER HITS ALLOWED (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401033

OVER
7401034

UNDER
Sep 09 2:10 PM
Stream

DAVID PETERSON - UNDER/OVER PITCHER RUNS EARNED (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401035

OVER
7401036

UNDER
Sep 09 2:10 PM
Stream

KENTA MAEDA - UNDER/OVER PITCHER RUNS EARNED (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401037

OVER
7401038

UNDER
Sep 09 2:10 PM
Stream

KENTA MAEDA - PITCHER TO RECORD THE WIN (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401039

NO
7401040

YES
Sep 09 2:10 PM
Stream

DAVID PETERSON - PITCHER TO RECORD THE WIN (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401041

NO
7401042

YES
Sep 09 2:10 PM
Stream

MERRILL KELLY - UNDER/OVER PITCHER OUTS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401043

OVER
7401044

UNDER
Sep 09 2:20 PM
Stream

JUSTIN STEELE - UNDER/OVER PITCHER OUTS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401045

OVER
7401046

UNDER
Sep 09 2:20 PM
Stream

MERRILL KELLY - UNDER/OVER PITCHER STRIKEOUTS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401047

OVER
7401048

UNDER
Sep 09 2:20 PM
Stream

JUSTIN STEELE - UNDER/OVER PITCHER STRIKEOUTS (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401049

OVER
7401050

UNDER
Sep 09 2:20 PM
Stream

JUSTIN STEELE - UNDER/OVER PITCHER HITS ALLOWED (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401051

OVER
7401052

UNDER
Sep 09 2:20 PM
Stream

MERRILL KELLY - UNDER/OVER PITCHER HITS ALLOWED (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401053

OVER
7401054

UNDER
Sep 09 2:20 PM
Stream

JUSTIN STEELE - UNDER/OVER PITCHER RUNS EARNED (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401055

OVER
7401056

UNDER
Sep 09 2:20 PM
Stream

MERRILL KELLY - UNDER/OVER PITCHER RUNS EARNED (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401057

OVER
7401058

UNDER
Sep 09 2:20 PM
Stream

JUSTIN STEELE - PITCHER TO RECORD THE WIN (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401059

NO
7401060

YES
Sep 09 2:20 PM
Stream

MERRILL KELLY - PITCHER TO RECORD THE WIN (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401061

NO
7401062

YES
Sep 09 2:20 PM
Stream

BOBBY MILLER - UNDER/OVER PITCHER OUTS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401063

OVER
7401064

UNDER
Sep 09 4:05 PM
Stream

JAKE IRVIN - UNDER/OVER PITCHER OUTS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401065

OVER
7401066

UNDER
Sep 09 4:05 PM
Stream

BOBBY MILLER - UNDER/OVER PITCHER STRIKEOUTS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401067

OVER
7401068

UNDER
Sep 09 4:05 PM
Stream

JAKE IRVIN - UNDER/OVER PITCHER STRIKEOUTS (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401069

OVER
7401070

UNDER
Sep 09 4:05 PM
Stream

JAKE IRVIN - UNDER/OVER PITCHER HITS ALLOWED (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401071

OVER
7401072

UNDER
Sep 09 4:05 PM
Stream

BOBBY MILLER - UNDER/OVER PITCHER HITS ALLOWED (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401073

OVER
7401074

UNDER
Sep 09 4:05 PM
Stream

BOBBY MILLER - UNDER/OVER PITCHER RUNS EARNED (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401075

OVER
7401076

UNDER
Sep 09 4:05 PM
Stream

JAKE IRVIN - UNDER/OVER PITCHER RUNS EARNED (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401077

OVER
7401078

UNDER
Sep 09 4:05 PM
Stream

JAKE IRVIN - PITCHER TO RECORD THE WIN (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401079

NO
7401080

YES
Sep 09 4:05 PM
Stream

BOBBY MILLER - PITCHER TO RECORD THE WIN (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401081

NO
7401082

YES
Sep 09 4:05 PM
Stream

AARON CIVALE - UNDER/OVER PITCHER OUTS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401083

OVER
7401084

UNDER
Sep 09 4:05 PM
Stream

AARON CIVALE - UNDER/OVER PITCHER STRIKEOUTS (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401085

OVER
7401086

UNDER
Sep 09 4:05 PM
Stream

AARON CIVALE - UNDER/OVER PITCHER HITS ALLOWED (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401087

OVER
7401088

UNDER
Sep 09 4:05 PM
Stream

AARON CIVALE - UNDER/OVER PITCHER RUNS EARNED (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401089

OVER
7401090

UNDER
Sep 09 4:05 PM
Stream

AARON CIVALE - PITCHER TO RECORD THE WIN (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401091

NO
7401092

YES
Sep 09 4:05 PM
Stream

CHRIS SALE - UNDER/OVER PITCHER OUTS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401093

OVER
7401094

UNDER
Sep 09 4:10 PM
Stream

JACK FLAHERTY - UNDER/OVER PITCHER OUTS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401095

OVER
7401096

UNDER
Sep 09 4:10 PM
Stream

CHRIS SALE - UNDER/OVER PITCHER STRIKEOUTS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401097

OVER
7401098

UNDER
Sep 09 4:10 PM
Stream

JACK FLAHERTY - UNDER/OVER PITCHER STRIKEOUTS (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401099

OVER
7401100

UNDER
Sep 09 4:10 PM
Stream

JACK FLAHERTY - UNDER/OVER PITCHER HITS ALLOWED (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401101

OVER
7401102

UNDER
Sep 09 4:10 PM
Stream

CHRIS SALE - UNDER/OVER PITCHER HITS ALLOWED (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401103

OVER
7401104

UNDER
Sep 09 4:10 PM
Stream

CHRIS SALE - UNDER/OVER PITCHER RUNS EARNED (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401105

OVER
7401106

UNDER
Sep 09 4:10 PM
Stream

JACK FLAHERTY - UNDER/OVER PITCHER RUNS EARNED (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401107

OVER
7401108

UNDER
Sep 09 4:10 PM
Stream

CHRIS SALE - PITCHER TO RECORD THE WIN (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401109

NO
7401110

YES
Sep 09 4:10 PM
Stream

JACK FLAHERTY - PITCHER TO RECORD THE WIN (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401111

NO
7401112

YES
Sep 09 4:10 PM
Stream

JOHNNY CUETO - UNDER/OVER PITCHER OUTS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401113

OVER
7401114

UNDER
Sep 09 6:05 PM
Stream

AARON NOLA - UNDER/OVER PITCHER OUTS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401115

OVER
7401116

UNDER
Sep 09 6:05 PM
Stream

AARON NOLA - UNDER/OVER PITCHER STRIKEOUTS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401117

OVER
7401118

UNDER
Sep 09 6:05 PM
Stream

JOHNNY CUETO - UNDER/OVER PITCHER STRIKEOUTS (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401119

OVER
7401120

UNDER
Sep 09 6:05 PM
Stream

JOHNNY CUETO - UNDER/OVER PITCHER HITS ALLOWED (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401121

OVER
7401122

UNDER
Sep 09 6:05 PM
Stream

AARON NOLA - UNDER/OVER PITCHER HITS ALLOWED (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401123

OVER
7401124

UNDER
Sep 09 6:05 PM
Stream

AARON NOLA - UNDER/OVER PITCHER RUNS EARNED (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401125

OVER
7401126

UNDER
Sep 09 6:05 PM
Stream

JOHNNY CUETO - UNDER/OVER PITCHER RUNS EARNED (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401127

OVER
7401128

UNDER
Sep 09 6:05 PM
Stream

JOHNNY CUETO - PITCHER TO RECORD THE WIN (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401129

NO
7401130

YES
Sep 09 6:05 PM
Stream

AARON NOLA - PITCHER TO RECORD THE WIN (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401131

NO
7401132

YES
Sep 09 6:05 PM
Stream

ZACHARY DAVID THOMPSON - UNDER/OVER PITCHER OUTS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401133

OVER
7401134

UNDER
Sep 09 6:40 PM
Stream

CARSON SPIERS - UNDER/OVER PITCHER STRIKEOUTS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401135

OVER
7401136

UNDER
Sep 09 6:40 PM
Stream

ZACHARY DAVID THOMPSON - UNDER/OVER PITCHER STRIKEOUTS (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401137

OVER
7401138

UNDER
Sep 09 6:40 PM
Stream

ZACHARY DAVID THOMPSON - UNDER/OVER PITCHER HITS ALLOWED (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401139

OVER
7401140

UNDER
Sep 09 6:40 PM
Stream

CARSON SPIERS - UNDER/OVER PITCHER HITS ALLOWED (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401141

OVER
7401142

UNDER
Sep 09 6:40 PM
Stream

CARSON SPIERS - UNDER/OVER PITCHER RUNS EARNED (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401143

OVER
7401144

UNDER
Sep 09 6:40 PM
Stream

ZACHARY DAVID THOMPSON - UNDER/OVER PITCHER RUNS EARNED (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401145

OVER
7401146

UNDER
Sep 09 6:40 PM
Stream

ZACHARY DAVID THOMPSON - PITCHER TO RECORD THE WIN (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401147

NO
7401148

YES
Sep 09 6:40 PM
Stream

SETH LUGO - UNDER/OVER PITCHER OUTS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401149

OVER
7401150

UNDER
Sep 09 7:10 PM
Stream

CRISTIAN JAVIER - UNDER/OVER PITCHER OUTS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401151

OVER
7401152

UNDER
Sep 09 7:10 PM
Stream

CRISTIAN JAVIER - UNDER/OVER PITCHER STRIKEOUTS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401153

OVER
7401154

UNDER
Sep 09 7:10 PM
Stream

SETH LUGO - UNDER/OVER PITCHER STRIKEOUTS (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401155

OVER
7401156

UNDER
Sep 09 7:10 PM
Stream

SETH LUGO - UNDER/OVER PITCHER HITS ALLOWED (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401157

OVER
7401158

UNDER
Sep 09 7:10 PM
Stream

CRISTIAN JAVIER - UNDER/OVER PITCHER HITS ALLOWED (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401159

OVER
7401160

UNDER
Sep 09 7:10 PM
Stream

CRISTIAN JAVIER - UNDER/OVER PITCHER RUNS EARNED (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401161

OVER
7401162

UNDER
Sep 09 7:10 PM
Stream

SETH LUGO - UNDER/OVER PITCHER RUNS EARNED (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401163

OVER
7401164

UNDER
Sep 09 7:10 PM
Stream

SETH LUGO - PITCHER TO RECORD THE WIN (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401165

NO
7401166

YES
Sep 09 7:10 PM
Stream

CRISTIAN JAVIER - PITCHER TO RECORD THE WIN (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401167

NO
7401168

YES
Sep 09 7:10 PM
Stream

JOHAN OVIEDO - UNDER/OVER PITCHER OUTS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401169

OVER
7401170

UNDER
Sep 09 7:20 PM
Stream

JOHAN OVIEDO - UNDER/OVER PITCHER STRIKEOUTS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401171

OVER
7401172

UNDER
Sep 09 7:20 PM
Stream

DYLAN DODD - UNDER/OVER PITCHER STRIKEOUTS (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401173

OVER
7401174

UNDER
Sep 09 7:20 PM
Stream

JOHAN OVIEDO - UNDER/OVER PITCHER HITS ALLOWED (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401175

OVER
7401176

UNDER
Sep 09 7:20 PM
Stream

DYLAN DODD - UNDER/OVER PITCHER HITS ALLOWED (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401177

OVER
7401178

UNDER
Sep 09 7:20 PM
Stream

DYLAN DODD - UNDER/OVER PITCHER RUNS EARNED (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401179

OVER
7401180

UNDER
Sep 09 7:20 PM
Stream

JOHAN OVIEDO - UNDER/OVER PITCHER RUNS EARNED (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401181

OVER
7401182

UNDER
Sep 09 7:20 PM
Stream

JOHAN OVIEDO - PITCHER TO RECORD THE WIN (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401183

NO
7401184

YES
Sep 09 7:20 PM
Stream

LOGAN WEBB - UNDER/OVER PITCHER OUTS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401185

OVER
7401186

UNDER
Sep 09 9:05 PM
Stream

LOGAN WEBB - UNDER/OVER PITCHER STRIKEOUTS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401187

OVER
7401188

UNDER
Sep 09 9:05 PM
Stream

CHASE ANDERSON - UNDER/OVER PITCHER STRIKEOUTS (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401189

OVER
7401190

UNDER
Sep 09 9:05 PM
Stream

LOGAN WEBB - UNDER/OVER PITCHER HITS ALLOWED (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401191

OVER
7401192

UNDER
Sep 09 9:05 PM
Stream

CHASE ANDERSON - UNDER/OVER PITCHER HITS ALLOWED (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401193

OVER
7401194

UNDER
Sep 09 9:05 PM
Stream

CHASE ANDERSON - UNDER/OVER PITCHER RUNS EARNED (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401195

OVER
7401196

UNDER
Sep 09 9:05 PM
Stream

LOGAN WEBB - UNDER/OVER PITCHER RUNS EARNED (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401197

OVER
7401198

UNDER
Sep 09 9:05 PM
Stream

LOGAN WEBB - PITCHER TO RECORD THE WIN (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401199

NO
7401200

YES
Sep 09 9:05 PM
Stream

LUCAS GIOLITO - UNDER/OVER PITCHER OUTS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401201

OVER
7401202

UNDER
Sep 09 9:07 PM
Stream

TYLER ANDERSON - UNDER/OVER PITCHER OUTS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401203

OVER
7401204

UNDER
Sep 09 9:07 PM
Stream

TYLER ANDERSON - UNDER/OVER PITCHER STRIKEOUTS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401205

OVER
7401206

UNDER
Sep 09 9:07 PM
Stream

LUCAS GIOLITO - UNDER/OVER PITCHER STRIKEOUTS (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401207

OVER
7401208

UNDER
Sep 09 9:07 PM
Stream

TYLER ANDERSON - UNDER/OVER PITCHER HITS ALLOWED (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401209

OVER
7401210

UNDER
Sep 09 9:07 PM
Stream

LUCAS GIOLITO - UNDER/OVER PITCHER HITS ALLOWED (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401211

OVER
7401212

UNDER
Sep 09 9:07 PM
Stream

LUCAS GIOLITO - UNDER/OVER PITCHER RUNS EARNED (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401213

OVER
7401214

UNDER
Sep 09 9:07 PM
Stream

TYLER ANDERSON - UNDER/OVER PITCHER RUNS EARNED (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401215

OVER
7401216

UNDER
Sep 09 9:07 PM
Stream

LUCAS GIOLITO - PITCHER TO RECORD THE WIN (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401217

NO
7401218

YES
Sep 09 9:07 PM
Stream

TYLER ANDERSON - PITCHER TO RECORD THE WIN (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7401219

NO
7401220

YES
Sep 09 9:07 PM
Stream

MLB - PLAYER TOTAL BASES (MUST START)
WILLIAM CONTRERAS - UNDER/OVER PLAYER TOTAL BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402003

OVER
7402004

UNDER
Sep 09 2:05 PM
Stream

ANTHONY VOLPE - UNDER/OVER PLAYER TOTAL BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402005

OVER
7402006

UNDER
Sep 09 2:05 PM
Stream

WILLY ADAMES - UNDER/OVER PLAYER TOTAL BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402007

OVER
7402008

UNDER
Sep 09 2:05 PM
Stream

CHRISTIAN YELICH - UNDER/OVER PLAYER TOTAL BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402009

OVER
7402010

UNDER
Sep 09 2:05 PM
Stream

ANDRUW MONASTERIO - UNDER/OVER PLAYER TOTAL BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402011

OVER
7402012

UNDER
Sep 09 2:05 PM
Stream

TYRONE TAYLOR - UNDER/OVER PLAYER TOTAL BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402013

OVER
7402014

UNDER
Sep 09 2:05 PM
Stream

GLEYBER TORRES - UNDER/OVER PLAYER TOTAL BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402015

OVER
7402016

UNDER
Sep 09 2:05 PM
Stream

OSWALD PERAZA - UNDER/OVER PLAYER TOTAL BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402017

OVER
7402018

UNDER
Sep 09 2:05 PM
Stream

JASSON DOMINGUEZ - UNDER/OVER PLAYER TOTAL BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402019

OVER
7402020

UNDER
Sep 09 2:05 PM
Stream

DAVID JOHN LEMAHIEU - UNDER/OVER PLAYER TOTAL BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402021

OVER
7402022

UNDER
Sep 09 2:05 PM
Stream

GIANCARLO STANTON - UNDER/OVER PLAYER TOTAL BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402023

OVER
7402024

UNDER
Sep 09 2:05 PM
Stream

BRICE TURANG - UNDER/OVER PLAYER TOTAL BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402025

OVER
7402026

UNDER
Sep 09 2:05 PM
Stream

KYLE HIGASHIOKA - UNDER/OVER PLAYER TOTAL BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402027

OVER
7402028

UNDER
Sep 09 2:05 PM
Stream

AARON JUDGE - UNDER/OVER PLAYER TOTAL BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402029

OVER
7402030

UNDER
Sep 09 2:05 PM
Stream

SAL FRELICK - UNDER/OVER PLAYER TOTAL BASES (New York Yankees vs Milwaukee Brewers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402031

OVER
7402032

UNDER
Sep 09 2:05 PM
Stream

KYLE FARMER - UNDER/OVER PLAYER TOTAL BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402033

OVER
7402034

UNDER
Sep 09 2:10 PM
Stream

BRANDON NIMMO - UNDER/OVER PLAYER TOTAL BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402035

OVER
7402036

UNDER
Sep 09 2:10 PM
Stream

BRETT BATY - UNDER/OVER PLAYER TOTAL BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402037

OVER
7402038

UNDER
Sep 09 2:10 PM
Stream

JORGE POLANCO - UNDER/OVER PLAYER TOTAL BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402039

OVER
7402040

UNDER
Sep 09 2:10 PM
Stream

RONNY MAURICIO - UNDER/OVER PLAYER TOTAL BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402041

OVER
7402042

UNDER
Sep 09 2:10 PM
Stream

FRANCISCO LINDOR - UNDER/OVER PLAYER TOTAL BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402043

OVER
7402044

UNDER
Sep 09 2:10 PM
Stream

CARLOS CORREA - UNDER/OVER PLAYER TOTAL BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402045

OVER
7402046

UNDER
Sep 09 2:10 PM
Stream

WILLI CASTRO - UNDER/OVER PLAYER TOTAL BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402047

OVER
7402048

UNDER
Sep 09 2:10 PM
Stream

MARK VIENTOS - UNDER/OVER PLAYER TOTAL BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402049

OVER
7402050

UNDER
Sep 09 2:10 PM
Stream

OMAR NARVAEZ - UNDER/OVER PLAYER TOTAL BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402051

OVER
7402052

UNDER
Sep 09 2:10 PM
Stream

DONOVAN SOLANO - UNDER/OVER PLAYER TOTAL BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402053

OVER
7402054

UNDER
Sep 09 2:10 PM
Stream

PETER ALONSO - UNDER/OVER PLAYER TOTAL BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402055

OVER
7402056

UNDER
Sep 09 2:10 PM
Stream

ROYCE LEWIS - UNDER/OVER PLAYER TOTAL BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402057

OVER
7402058

UNDER
Sep 09 2:10 PM
Stream

RAFAEL ORTEGA - UNDER/OVER PLAYER TOTAL BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402059

OVER
7402060

UNDER
Sep 09 2:10 PM
Stream

JEFF MCNEIL - UNDER/OVER PLAYER TOTAL BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402061

OVER
7402062

UNDER
Sep 09 2:10 PM
Stream

JORDAN LUPLOW - UNDER/OVER PLAYER TOTAL BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402063

OVER
7402064

UNDER
Sep 09 2:10 PM
Stream

RYAN JEFFERS - UNDER/OVER PLAYER TOTAL BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402065

OVER
7402066

UNDER
Sep 09 2:10 PM
Stream

MATT WALLNER - UNDER/OVER PLAYER TOTAL BASES (Minnesota Twins vs New York Mets) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402067

OVER
7402068

UNDER
Sep 09 2:10 PM
Stream

CODY BELLINGER - UNDER/OVER PLAYER TOTAL BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402069

OVER
7402070

UNDER
Sep 09 2:20 PM
Stream

DANSBY SWANSON - UNDER/OVER PLAYER TOTAL BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402071

OVER
7402072

UNDER
Sep 09 2:20 PM
Stream

MIKE TAUCHMAN - UNDER/OVER PLAYER TOTAL BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402073

OVER
7402074

UNDER
Sep 09 2:20 PM
Stream

CORBIN CARROLL - UNDER/OVER PLAYER TOTAL BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402075

OVER
7402076

UNDER
Sep 09 2:20 PM
Stream

EMMANUEL RIVERA - UNDER/OVER PLAYER TOTAL BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402077

OVER
7402078

UNDER
Sep 09 2:20 PM
Stream

EVAN LONGORIA - UNDER/OVER PLAYER TOTAL BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402079

OVER
7402080

UNDER
Sep 09 2:20 PM
Stream

TOMMY PHAM - UNDER/OVER PLAYER TOTAL BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402081

OVER
7402082

UNDER
Sep 09 2:20 PM
Stream

GERALDO PERDOMO - UNDER/OVER PLAYER TOTAL BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402083

OVER
7402084

UNDER
Sep 09 2:20 PM
Stream

NICK MADRIGAL - UNDER/OVER PLAYER TOTAL BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402085

OVER
7402086

UNDER
Sep 09 2:20 PM
Stream

NICO HOERNER - UNDER/OVER PLAYER TOTAL BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402087

OVER
7402088

UNDER
Sep 09 2:20 PM
Stream

SEIYA SUZUKI - UNDER/OVER PLAYER TOTAL BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402089

OVER
7402090

UNDER
Sep 09 2:20 PM
Stream

IAN HAPP - UNDER/OVER PLAYER TOTAL BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402091

OVER
7402092

UNDER
Sep 09 2:20 PM
Stream

CHRISTIAN WALKER - UNDER/OVER PLAYER TOTAL BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402093

OVER
7402094

UNDER
Sep 09 2:20 PM
Stream

LOURDES GURRIEL - UNDER/OVER PLAYER TOTAL BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402095

OVER
7402096

UNDER
Sep 09 2:20 PM
Stream

GABRIEL MORENO - UNDER/OVER PLAYER TOTAL BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402097

OVER
7402098

UNDER
Sep 09 2:20 PM
Stream

KETEL MARTE - UNDER/OVER PLAYER TOTAL BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402099

OVER
7402100

UNDER
Sep 09 2:20 PM
Stream

JEIMER CANDELARIO - UNDER/OVER PLAYER TOTAL BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402101

OVER
7402102

UNDER
Sep 09 2:20 PM
Stream

YAN GOMES - UNDER/OVER PLAYER TOTAL BASES (Chicago Cubs vs Arizona Diamondbacks) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402103

OVER
7402104

UNDER
Sep 09 2:20 PM
Stream

LANE THOMAS - UNDER/OVER PLAYER TOTAL BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402105

OVER
7402106

UNDER
Sep 09 4:05 PM
Stream

FREDDIE FREEMAN - UNDER/OVER PLAYER TOTAL BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402107

OVER
7402108

UNDER
Sep 09 4:05 PM
Stream

MIGUEL ROJAS - UNDER/OVER PLAYER TOTAL BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402109

OVER
7402110

UNDER
Sep 09 4:05 PM
Stream

ENRIQUE HERNANDEZ - UNDER/OVER PLAYER TOTAL BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402111

OVER
7402112

UNDER
Sep 09 4:05 PM
Stream

JASON HEYWARD - UNDER/OVER PLAYER TOTAL BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402113

OVER
7402114

UNDER
Sep 09 4:05 PM
Stream

JAMES OUTMAN - UNDER/OVER PLAYER TOTAL BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402115

OVER
7402116

UNDER
Sep 09 4:05 PM
Stream

MAX MUNCY - UNDER/OVER PLAYER TOTAL BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402117

OVER
7402118

UNDER
Sep 09 4:05 PM
Stream

CJ ABRAMS - UNDER/OVER PLAYER TOTAL BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402119

OVER
7402120

UNDER
Sep 09 4:05 PM
Stream

DAVID PERALTA - UNDER/OVER PLAYER TOTAL BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402121

OVER
7402122

UNDER
Sep 09 4:05 PM
Stream

DOMINIC SMITH - UNDER/OVER PLAYER TOTAL BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402123

OVER
7402124

UNDER
Sep 09 4:05 PM
Stream

CARTER KIEBOOM - UNDER/OVER PLAYER TOTAL BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402125

OVER
7402126

UNDER
Sep 09 4:05 PM
Stream

JACOB YOUNG - UNDER/OVER PLAYER TOTAL BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402127

OVER
7402128

UNDER
Sep 09 4:05 PM
Stream

ALEX CALL - UNDER/OVER PLAYER TOTAL BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402129

OVER
7402130

UNDER
Sep 09 4:05 PM
Stream

JAKE ALU - UNDER/OVER PLAYER TOTAL BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402131

OVER
7402132

UNDER
Sep 09 4:05 PM
Stream

WILL SMITH - UNDER/OVER PLAYER TOTAL BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402133

OVER
7402134

UNDER
Sep 09 4:05 PM
Stream

KEIBERT RUIZ - UNDER/OVER PLAYER TOTAL BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402135

OVER
7402136

UNDER
Sep 09 4:05 PM
Stream

J.D. MARTINEZ - UNDER/OVER PLAYER TOTAL BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402137

OVER
7402138

UNDER
Sep 09 4:05 PM
Stream

JOEY MENESES - UNDER/OVER PLAYER TOTAL BASES (Washington Nationals vs Los Angeles Dodgers) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402139

OVER
7402140

UNDER
Sep 09 4:05 PM
Stream

DOMINIC CANZONE - UNDER/OVER PLAYER TOTAL BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402141

OVER
7402142

UNDER
Sep 09 4:05 PM
Stream

J.P. CRAWFORD - UNDER/OVER PLAYER TOTAL BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402143

OVER
7402144

UNDER
Sep 09 4:05 PM
Stream

TY FRANCE - UNDER/OVER PLAYER TOTAL BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402145

OVER
7402146

UNDER
Sep 09 4:05 PM
Stream

JOSE SIRI - UNDER/OVER PLAYER TOTAL BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402147

OVER
7402148

UNDER
Sep 09 4:05 PM
Stream

JOSH LOWE - UNDER/OVER PLAYER TOTAL BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402149

OVER
7402150

UNDER
Sep 09 4:05 PM
Stream

TAYLOR WALLS - UNDER/OVER PLAYER TOTAL BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402151

OVER
7402152

UNDER
Sep 09 4:05 PM
Stream

CHRISTIAN BETHANCOURT - UNDER/OVER PLAYER TOTAL BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402153

OVER
7402154

UNDER
Sep 09 4:05 PM
Stream

ISAAC PAREDES - UNDER/OVER PLAYER TOTAL BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402155

OVER
7402156

UNDER
Sep 09 4:05 PM
Stream

YANDY DIAZ - UNDER/OVER PLAYER TOTAL BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402157

OVER
7402158

UNDER
Sep 09 4:05 PM
Stream

EUGENIO SUAREZ - UNDER/OVER PLAYER TOTAL BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402159

OVER
7402160

UNDER
Sep 09 4:05 PM
Stream

RANDY AROZARENA - UNDER/OVER PLAYER TOTAL BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402161

OVER
7402162

UNDER
Sep 09 4:05 PM
Stream

TEOSCAR HERNÁNDEZ - UNDER/OVER PLAYER TOTAL BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402163

OVER
7402164

UNDER
Sep 09 4:05 PM
Stream

MIKE FORD - UNDER/OVER PLAYER TOTAL BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402165

OVER
7402166

UNDER
Sep 09 4:05 PM
Stream

LUKE RALEY - UNDER/OVER PLAYER TOTAL BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402167

OVER
7402168

UNDER
Sep 09 4:05 PM
Stream

JULIO RODRIGUEZ - UNDER/OVER PLAYER TOTAL BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402169

OVER
7402170

UNDER
Sep 09 4:05 PM
Stream

JOSHUA ROJAS - UNDER/OVER PLAYER TOTAL BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402171

OVER
7402172

UNDER
Sep 09 4:05 PM
Stream

BRANDON LOWE - UNDER/OVER PLAYER TOTAL BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402173

OVER
7402174

UNDER
Sep 09 4:05 PM
Stream

CAL RALEIGH - UNDER/OVER PLAYER TOTAL BASES (Tampa Bay Rays vs Seattle Mariners) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402175

OVER
7402176

UNDER
Sep 09 4:05 PM
Stream

CONNOR WONG - UNDER/OVER PLAYER TOTAL BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402177

OVER
7402178

UNDER
Sep 09 4:10 PM
Stream

TREVOR STORY - UNDER/OVER PLAYER TOTAL BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402179

OVER
7402180

UNDER
Sep 09 4:10 PM
Stream

ADAM DUVALL - UNDER/OVER PLAYER TOTAL BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402181

OVER
7402182

UNDER
Sep 09 4:10 PM
Stream

ADLEY RUTSCHMAN - UNDER/OVER PLAYER TOTAL BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402183

OVER
7402184

UNDER
Sep 09 4:10 PM
Stream

ANTHONY SANTANDER - UNDER/OVER PLAYER TOTAL BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402185

OVER
7402186

UNDER
Sep 09 4:10 PM
Stream

AARON HICKS - UNDER/OVER PLAYER TOTAL BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402187

OVER
7402188

UNDER
Sep 09 4:10 PM
Stream

ALEX VERDUGO - UNDER/OVER PLAYER TOTAL BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402189

OVER
7402190

UNDER
Sep 09 4:10 PM
Stream

RAFAEL DEVERS - UNDER/OVER PLAYER TOTAL BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402191

OVER
7402192

UNDER
Sep 09 4:10 PM
Stream

JUSTIN TURNER - UNDER/OVER PLAYER TOTAL BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402193

OVER
7402194

UNDER
Sep 09 4:10 PM
Stream

RYAN MOUNTCASTLE - UNDER/OVER PLAYER TOTAL BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402195

OVER
7402196

UNDER
Sep 09 4:10 PM
Stream

JAMES MCCANN - UNDER/OVER PLAYER TOTAL BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402197

OVER
7402198

UNDER
Sep 09 4:10 PM
Stream

GUNNAR HENDERSON - UNDER/OVER PLAYER TOTAL BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402199

OVER
7402200

UNDER
Sep 09 4:10 PM
Stream

RAMON URIAS - UNDER/OVER PLAYER TOTAL BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402201

OVER
7402202

UNDER
Sep 09 4:10 PM
Stream

TRISTON CASAS - UNDER/OVER PLAYER TOTAL BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402203

OVER
7402204

UNDER
Sep 09 4:10 PM
Stream

AUSTIN HAYS - UNDER/OVER PLAYER TOTAL BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402205

OVER
7402206

UNDER
Sep 09 4:10 PM
Stream

JORGE MATEO - UNDER/OVER PLAYER TOTAL BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402207

OVER
7402208

UNDER
Sep 09 4:10 PM
Stream

MASATAKA YOSHIDA - UNDER/OVER PLAYER TOTAL BASES (Boston Red Sox vs Baltimore Orioles) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402209

OVER
7402210

UNDER
Sep 09 4:10 PM
Stream

J.T. REALMUTO - UNDER/OVER PLAYER TOTAL BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402211

OVER
7402212

UNDER
Sep 09 6:05 PM
Stream

JACOB MICHAEL BURGER - UNDER/OVER PLAYER TOTAL BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402213

OVER
7402214

UNDER
Sep 09 6:05 PM
Stream

BRYSON STOTT - UNDER/OVER PLAYER TOTAL BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402215

OVER
7402216

UNDER
Sep 09 6:05 PM
Stream

ALEC BOHM - UNDER/OVER PLAYER TOTAL BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402217

OVER
7402218

UNDER
Sep 09 6:05 PM
Stream

TREA TURNER - UNDER/OVER PLAYER TOTAL BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402219

OVER
7402220

UNDER
Sep 09 6:05 PM
Stream

JAZZ CHISHOLM - UNDER/OVER PLAYER TOTAL BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402221

OVER
7402222

UNDER
Sep 09 6:05 PM
Stream

BRYCE HARPER - UNDER/OVER PLAYER TOTAL BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402223

OVER
7402224

UNDER
Sep 09 6:05 PM
Stream

BRANDON MARSH - UNDER/OVER PLAYER TOTAL BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402225

OVER
7402226

UNDER
Sep 09 6:05 PM
Stream

JESUS SANCHEZ - UNDER/OVER PLAYER TOTAL BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402227

OVER
7402228

UNDER
Sep 09 6:05 PM
Stream

BRYAN DE LA CRUZ - UNDER/OVER PLAYER TOTAL BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402229

OVER
7402230

UNDER
Sep 09 6:05 PM
Stream

LUIS ARRAEZ - UNDER/OVER PLAYER TOTAL BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402231

OVER
7402232

UNDER
Sep 09 6:05 PM
Stream

JOSHUA EVAN BELL - UNDER/OVER PLAYER TOTAL BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402233

OVER
7402234

UNDER
Sep 09 6:05 PM
Stream

JOEY WENDLE - UNDER/OVER PLAYER TOTAL BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402235

OVER
7402236

UNDER
Sep 09 6:05 PM
Stream

NICK CASTELLANOS - UNDER/OVER PLAYER TOTAL BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402237

OVER
7402238

UNDER
Sep 09 6:05 PM
Stream

JAKE CAVE - UNDER/OVER PLAYER TOTAL BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402239

OVER
7402240

UNDER
Sep 09 6:05 PM
Stream

NICK FORTES - UNDER/OVER PLAYER TOTAL BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402241

OVER
7402242

UNDER
Sep 09 6:05 PM
Stream

KYLE SCHWARBER - UNDER/OVER PLAYER TOTAL BASES (Philadelphia Phillies vs Miami Marlins) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402243

OVER
7402244

UNDER
Sep 09 6:05 PM
Stream

LARS NOOTBAAR - UNDER/OVER PLAYER TOTAL BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402245

OVER
7402246

UNDER
Sep 09 6:40 PM
Stream

ELLY DE LA CRUZ - UNDER/OVER PLAYER TOTAL BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402247

OVER
7402248

UNDER
Sep 09 6:40 PM
Stream

TOMMY EDMAN - UNDER/OVER PLAYER TOTAL BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402249

OVER
7402250

UNDER
Sep 09 6:40 PM
Stream

JORDAN WALKER - UNDER/OVER PLAYER TOTAL BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402251

OVER
7402252

UNDER
Sep 09 6:40 PM
Stream

WILLSON CONTRERAS - UNDER/OVER PLAYER TOTAL BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402253

OVER
7402254

UNDER
Sep 09 6:40 PM
Stream

SPENCER STEER - UNDER/OVER PLAYER TOTAL BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402255

OVER
7402256

UNDER
Sep 09 6:40 PM
Stream

CHRISTIAN ENCARNACION-STRAND - UNDER/OVER PLAYER TOTAL BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402257

OVER
7402258

UNDER
Sep 09 6:40 PM
Stream

NOLAN GORMAN - UNDER/OVER PLAYER TOTAL BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402259

OVER
7402260

UNDER
Sep 09 6:40 PM
Stream

MASYN WINN - UNDER/OVER PLAYER TOTAL BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402261

OVER
7402262

UNDER
Sep 09 6:40 PM
Stream

TYLER STEPHENSON - UNDER/OVER PLAYER TOTAL BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402263

OVER
7402264

UNDER
Sep 09 6:40 PM
Stream

STUART FAIRCHILD - UNDER/OVER PLAYER TOTAL BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402265

OVER
7402266

UNDER
Sep 09 6:40 PM
Stream

TYLER O'NEILL - UNDER/OVER PLAYER TOTAL BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402267

OVER
7402268

UNDER
Sep 09 6:40 PM
Stream

NICK SENZEL - UNDER/OVER PLAYER TOTAL BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402269

OVER
7402270

UNDER
Sep 09 6:40 PM
Stream

PAUL GOLDSCHMIDT - UNDER/OVER PLAYER TOTAL BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402271

OVER
7402272

UNDER
Sep 09 6:40 PM
Stream

HUNTER RENFROE - UNDER/OVER PLAYER TOTAL BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402273

OVER
7402274

UNDER
Sep 09 6:40 PM
Stream

HARRISON BADER - UNDER/OVER PLAYER TOTAL BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402275

OVER
7402276

UNDER
Sep 09 6:40 PM
Stream

NOLAN ARENADO - UNDER/OVER PLAYER TOTAL BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402277

OVER
7402278

UNDER
Sep 09 6:40 PM
Stream

NOELVI MARTE - UNDER/OVER PLAYER TOTAL BASES (Cincinnati Reds vs St. Louis Cardinals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402279

OVER
7402280

UNDER
Sep 09 6:40 PM
Stream

KYLE TUCKER - UNDER/OVER PLAYER TOTAL BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402281

OVER
7402282

UNDER
Sep 09 7:10 PM
Stream

MARTIN MALDONADO - UNDER/OVER PLAYER TOTAL BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402283

OVER
7402284

UNDER
Sep 09 7:10 PM
Stream

HA-SEONG KIM - UNDER/OVER PLAYER TOTAL BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402285

OVER
7402286

UNDER
Sep 09 7:10 PM
Stream

TRENT GRISHAM - UNDER/OVER PLAYER TOTAL BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402287

OVER
7402288

UNDER
Sep 09 7:10 PM
Stream

LUIS CAMPUSANO - UNDER/OVER PLAYER TOTAL BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402289

OVER
7402290

UNDER
Sep 09 7:10 PM
Stream

FERNANDO TATIS JR. - UNDER/OVER PLAYER TOTAL BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402291

OVER
7402292

UNDER
Sep 09 7:10 PM
Stream

JUAN SOTO - UNDER/OVER PLAYER TOTAL BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402293

OVER
7402294

UNDER
Sep 09 7:10 PM
Stream

MAURICIO DUBÓN - UNDER/OVER PLAYER TOTAL BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402295

OVER
7402296

UNDER
Sep 09 7:10 PM
Stream

JOSE ABREU - UNDER/OVER PLAYER TOTAL BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402297

OVER
7402298

UNDER
Sep 09 7:10 PM
Stream

YORDAN ALVAREZ - UNDER/OVER PLAYER TOTAL BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402299

OVER
7402300

UNDER
Sep 09 7:10 PM
Stream

JEREMY PENA - UNDER/OVER PLAYER TOTAL BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402301

OVER
7402302

UNDER
Sep 09 7:10 PM
Stream

MANNY MACHADO - UNDER/OVER PLAYER TOTAL BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402303

OVER
7402304

UNDER
Sep 09 7:10 PM
Stream

ALEX BREGMAN - UNDER/OVER PLAYER TOTAL BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402305

OVER
7402306

UNDER
Sep 09 7:10 PM
Stream

MICHAEL BRANTLEY - UNDER/OVER PLAYER TOTAL BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402307

OVER
7402308

UNDER
Sep 09 7:10 PM
Stream

GARRETT COOPER - UNDER/OVER PLAYER TOTAL BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402309

OVER
7402310

UNDER
Sep 09 7:10 PM
Stream

JOSE ALTUVE - UNDER/OVER PLAYER TOTAL BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402311

OVER
7402312

UNDER
Sep 09 7:10 PM
Stream

XANDER BOGAERTS - UNDER/OVER PLAYER TOTAL BASES (Houston Astros vs San Diego Padres) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402313

OVER
7402314

UNDER
Sep 09 7:10 PM
Stream

ORLANDO ARCIA - UNDER/OVER PLAYER TOTAL BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402315

OVER
7402316

UNDER
Sep 09 7:20 PM
Stream

BRYAN REYNOLDS - UNDER/OVER PLAYER TOTAL BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402317

OVER
7402318

UNDER
Sep 09 7:20 PM
Stream

MICHAEL HARRIS - UNDER/OVER PLAYER TOTAL BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402319

OVER
7402320

UNDER
Sep 09 7:20 PM
Stream

KE'BRYAN HAYES - UNDER/OVER PLAYER TOTAL BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402321

OVER
7402322

UNDER
Sep 09 7:20 PM
Stream

LIOVER PEGUERO - UNDER/OVER PLAYER TOTAL BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402323

OVER
7402324

UNDER
Sep 09 7:20 PM
Stream

OZZIE ALBIES - UNDER/OVER PLAYER TOTAL BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402325

OVER
7402326

UNDER
Sep 09 7:20 PM
Stream

MATT OLSON - UNDER/OVER PLAYER TOTAL BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402327

OVER
7402328

UNDER
Sep 09 7:20 PM
Stream

RONALD ACUNA - UNDER/OVER PLAYER TOTAL BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402329

OVER
7402330

UNDER
Sep 09 7:20 PM
Stream

CONNOR JOE - UNDER/OVER PLAYER TOTAL BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402331

OVER
7402332

UNDER
Sep 09 7:20 PM
Stream

MARCELL OZUNA - UNDER/OVER PLAYER TOTAL BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402333

OVER
7402334

UNDER
Sep 09 7:20 PM
Stream

JI-HWAN BAE - UNDER/OVER PLAYER TOTAL BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402335

OVER
7402336

UNDER
Sep 09 7:20 PM
Stream

JARED TRIOLO - UNDER/OVER PLAYER TOTAL BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402337

OVER
7402338

UNDER
Sep 09 7:20 PM
Stream

ENDY RODRIGUEZ - UNDER/OVER PLAYER TOTAL BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402339

OVER
7402340

UNDER
Sep 09 7:20 PM
Stream

TRAVIS D'ARNAUD - UNDER/OVER PLAYER TOTAL BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402341

OVER
7402342

UNDER
Sep 09 7:20 PM
Stream

EDDIE ROSARIO - UNDER/OVER PLAYER TOTAL BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402343

OVER
7402344

UNDER
Sep 09 7:20 PM
Stream

MIGUEL ANDÚJAR - UNDER/OVER PLAYER TOTAL BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402345

OVER
7402346

UNDER
Sep 09 7:20 PM
Stream

AUSTIN RILEY - UNDER/OVER PLAYER TOTAL BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402347

OVER
7402348

UNDER
Sep 09 7:20 PM
Stream

ALIKA WILLIAMS - UNDER/OVER PLAYER TOTAL BASES (Atlanta Braves vs Pittsburgh Pirates) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402349

OVER
7402350

UNDER
Sep 09 7:20 PM
Stream

JOC PEDERSON - UNDER/OVER PLAYER TOTAL BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402351

OVER
7402352

UNDER
Sep 09 9:05 PM
Stream

NOLAN JONES - UNDER/OVER PLAYER TOTAL BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402353

OVER
7402354

UNDER
Sep 09 9:05 PM
Stream

JONATHAN GREGORY J D DAVIS - UNDER/OVER PLAYER TOTAL BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402355

OVER
7402356

UNDER
Sep 09 9:05 PM
Stream

LAMONTE WADE - UNDER/OVER PLAYER TOTAL BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402357

OVER
7402358

UNDER
Sep 09 9:05 PM
Stream

MIKE YASTRZEMSKI - UNDER/OVER PLAYER TOTAL BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402359

OVER
7402360

UNDER
Sep 09 9:05 PM
Stream

BLAKE SABOL - UNDER/OVER PLAYER TOTAL BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402361

OVER
7402362

UNDER
Sep 09 9:05 PM
Stream

BRENTON DOYLE - UNDER/OVER PLAYER TOTAL BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402363

OVER
7402364

UNDER
Sep 09 9:05 PM
Stream

EZEQUIEL TOVAR - UNDER/OVER PLAYER TOTAL BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402365

OVER
7402366

UNDER
Sep 09 9:05 PM
Stream

ELEHURIS MONTERO - UNDER/OVER PLAYER TOTAL BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402367

OVER
7402368

UNDER
Sep 09 9:05 PM
Stream

THAIRO ESTRADA - UNDER/OVER PLAYER TOTAL BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402369

OVER
7402370

UNDER
Sep 09 9:05 PM
Stream

CHARLIE BLACKMON - UNDER/OVER PLAYER TOTAL BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402371

OVER
7402372

UNDER
Sep 09 9:05 PM
Stream

RYAN MCMAHON - UNDER/OVER PLAYER TOTAL BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402373

OVER
7402374

UNDER
Sep 09 9:05 PM
Stream

BRENDAN RODGERS - UNDER/OVER PLAYER TOTAL BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402375

OVER
7402376

UNDER
Sep 09 9:05 PM
Stream

ELIAS DIAZ - UNDER/OVER PLAYER TOTAL BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402377

OVER
7402378

UNDER
Sep 09 9:05 PM
Stream

WILMER FLORES - UNDER/OVER PLAYER TOTAL BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402379

OVER
7402380

UNDER
Sep 09 9:05 PM
Stream

BRANDON CRAWFORD - UNDER/OVER PLAYER TOTAL BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402381

OVER
7402382

UNDER
Sep 09 9:05 PM
Stream

MITCHELL HANIGER - UNDER/OVER PLAYER TOTAL BASES (San Francisco Giants vs Colorado Rockies) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402383

OVER
7402384

UNDER
Sep 09 9:05 PM
Stream

JOSH NAYLOR - UNDER/OVER PLAYER TOTAL BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402385

OVER
7402386

UNDER
Sep 09 9:07 PM
Stream

KYREN PARIS - UNDER/OVER PLAYER TOTAL BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402387

OVER
7402388

UNDER
Sep 09 9:07 PM
Stream

KOLE CALHOUN - UNDER/OVER PLAYER TOTAL BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402389

OVER
7402390

UNDER
Sep 09 9:07 PM
Stream

NOLAN SCHANUEL - UNDER/OVER PLAYER TOTAL BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402391

OVER
7402392

UNDER
Sep 09 9:07 PM
Stream

MYLES STRAW - UNDER/OVER PLAYER TOTAL BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402393

OVER
7402394

UNDER
Sep 09 9:07 PM
Stream

LOGAN O'HOPPE - UNDER/OVER PLAYER TOTAL BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402395

OVER
7402396

UNDER
Sep 09 9:07 PM
Stream

JOSE RAMIREZ - UNDER/OVER PLAYER TOTAL BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402397

OVER
7402398

UNDER
Sep 09 9:07 PM
Stream

GABRIEL ARIAS - UNDER/OVER PLAYER TOTAL BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402399

OVER
7402400

UNDER
Sep 09 9:07 PM
Stream

ANDRES GIMENEZ - UNDER/OVER PLAYER TOTAL BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402401

OVER
7402402

UNDER
Sep 09 9:07 PM
Stream

RANDAL GRICHUK - UNDER/OVER PLAYER TOTAL BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402403

OVER
7402404

UNDER
Sep 09 9:07 PM
Stream

MIKE MOUSTAKAS - UNDER/OVER PLAYER TOTAL BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402405

OVER
7402406

UNDER
Sep 09 9:07 PM
Stream

STEVEN KWAN - UNDER/OVER PLAYER TOTAL BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402407

OVER
7402408

UNDER
Sep 09 9:07 PM
Stream

BRANDON DRURY - UNDER/OVER PLAYER TOTAL BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402409

OVER
7402410

UNDER
Sep 09 9:07 PM
Stream

RAMON LAUREANO - UNDER/OVER PLAYER TOTAL BASES (Los Angeles Angels vs Cleveland Guardians) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402411

OVER
7402412

UNDER
Sep 09 9:07 PM
Stream

MICHAEL MASSEY - UNDER/OVER PLAYER TOTAL BASES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402413

OVER
7402414

UNDER
Sep 09 3:07 PM
Stream

MAIKEL GARCIA - UNDER/OVER PLAYER TOTAL BASES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402415

OVER
7402416

UNDER
Sep 09 3:07 PM
Stream

MJ MELENDEZ - UNDER/OVER PLAYER TOTAL BASES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402417

OVER
7402418

UNDER
Sep 09 3:07 PM
Stream

DREW WATERS - UNDER/OVER PLAYER TOTAL BASES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402419

OVER
7402420

UNDER
Sep 09 3:07 PM
Stream

SALVADOR PEREZ - UNDER/OVER PLAYER TOTAL BASES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402421

OVER
7402422

UNDER
Sep 09 3:07 PM
Stream

BOBBY WITT JR. - UNDER/OVER PLAYER TOTAL BASES (Toronto Blue Jays vs Kansas City Royals) -

Rot

Team

Pitcher

M Line

Total

Run Line
7402423

OVER
7402424

UNDER
Sep 09 3:07 PM
"""

# Use regular expressions to find the matchups and corresponding Run Line numbers for each category
categories = ["SINGLES", "DOUBLES", "STOLEN BASES", "UNDER/OVER PITCHER", "UNDER/OVER PLAYER TOTAL BASES", "HOME RUNS", "PLAYER RUNS"]
matchup_run_line = {}

for category in categories:
    pattern = rf"{category}.*?\((.*?)\).*?Run Line\n(\d+)"
    matches = re.findall(pattern, text, re.DOTALL)

    if matches:
        matchup_run_line[category] = [{"Matchup": match[0], "Run Line": match[1]} for match in matches]

# Store the output of the original code in a variable
data = ""
for category, data_list in matchup_run_line.items():
    data += f"Category: {category}\n"
    for data_item in data_list:
        data += f"Matchup: {data_item['Matchup']}\n"
        data += f"Run Line: {data_item['Run Line']}\n"

# New logic to process the extracted data
sections = data.strip().split("Category: ")

# Initialize a dictionary to store the extracted run lines
run_lines = {}

# Iterate through the sections
for section in sections[1:]:  # Skip the first empty section
    lines = section.strip().split("\n")
    category = lines[0]  # Get the category name
    matchups = re.findall(r"Matchup: (.+)", section)
    run_lines[category] = {}

    for matchup in matchups:
        run_line = re.search(rf"Matchup: {re.escape(matchup)}\nRun Line: (\d+)", section)
        if run_line:
            run_lines[category][matchup] = run_line.group(1)

# Print the extracted run lines in the format of the new logic
for category, matchups in run_lines.items():
    print(f"Category: {category}")
    for matchup, run_line in matchups.items():
        print(f"Matchup: {matchup}")
        print(f"Run Line: {run_line}")