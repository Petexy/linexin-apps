# Maintainer: Petexy <https://github.com/Petexy>

pkgname=linexin-center
pkgver=1.1.0.r
pkgrel=1
_currentdate=$(date +"%Y-%m-%d%H-%M-%S")
pkgdesc='Linexin Center'
url='https://github.com/Petexy'
arch=(x86_64)
license=('GPL-3.0')
depends=(
  python-gobject
  gtk4
  libadwaita
  python
)
makedepends=(
)

package() {
   mkdir -p ${pkgdir}/usr/share/linexin/widgets
   mkdir -p ${pkgdir}/usr/bin
   mkdir -p ${pkgdir}/usr/applications
   mkdir -p ${pkgdir}/usr/icons   
   cp -rf ${srcdir}/usr/ ${pkgdir}/
}
