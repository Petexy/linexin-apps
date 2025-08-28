# Maintainer: Petexy <https://github.com/Petexy>

pkgname=linexin-tools
pkgver=0.8.0.r
pkgrel=1
_currentdate=$(date +"%Y-%m-%d%H-%M-%S")
pkgdesc='Linexin Tools'
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
   cp -rf ${srcdir}/usr/ ${pkgdir}/
}
