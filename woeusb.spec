%global debug_package   %{nil}
	
 
	
Name:           WoeUSB
	
Version:        3.2.12
	
Release:        2%{?dist}
	
Summary:        Windows USB installation media creator
	
License:        GPLv3+
	
URL:            https://github.com/slacka/WoeUSB
	
Source0:        https://github.com/slacka/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
	
 
	
Requires:       grub2-pc-modules
	
BuildRequires:  gcc
	
BuildRequires:  gcc-c++
	
BuildRequires:  wxGTK3-devel
	
BuildRequires:  autoconf
	
BuildRequires:  automake
	
BuildRequires:  libtool
	
BuildRequires:  gettext
	
BuildRequires:  desktop-file-utils
	
 
	
%description
	
A utility that enables you to create your own bootable Windows installation
	
USB storage device from an existing Windows Installation disc or disk image.
	
 
	
%prep
	
%autosetup
	
	
%build
	
# Replace the version placeholders
	
find . -type f -print0 | xargs -0 sed -i "s/@@WOEUSB_VERSION@@/%{version}/"
	
autoreconf -fiv
	
%configure
	
%make_build
	
	
%install
	
%make_install
	
sed -i '1!b;s/env bash/bash/' %{buildroot}%{_bindir}/woeusb
	
sed -i '1!b;s/env bash/bash/' %{buildroot}%{_datadir}/woeusb/data/listDvdDrive
	
sed -i '1!b;s/env bash/bash/' %{buildroot}%{_datadir}/woeusb/data/listUsb
	
# rpmgrill fails if the desktop icon is only in /usr/share/pixmaps (bug #1539633)
	
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
	
mv %{buildroot}%{_datadir}/pixmaps/woeusbgui-icon.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
	
desktop-file-validate %{buildroot}%{_datadir}/applications/woeusbgui.desktop
	
 
	
 
	
%files
	
%license COPYING
	
# CLI
	
%{_bindir}/woeusb
	
%{_mandir}/man1/woeusb.1.gz
	
# GUI
	
%{_mandir}/man1/woeusbgui.1.gz
	
%{_bindir}/woeusbgui
	
%{_datadir}/applications/woeusbgui.desktop
	
%{_datadir}/icons/hicolor/48x48/apps/woeusbgui-icon.png
	
%dir %{_datadir}/woeusb
	
%dir %{_datadir}/woeusb/data
	
%{_datadir}/woeusb/data/c501-logo.png
	
%{_datadir}/woeusb/data/icon.png
	
%{_datadir}/woeusb/data/listDvdDrive
	
%{_datadir}/woeusb/data/listUsb
	
%{_datadir}/woeusb/data/woeusb-logo.png
	
%dir %{_datadir}/woeusb/locale
	
%dir %{_datadir}/woeusb/locale/fr
	
%dir %{_datadir}/woeusb/locale/fr/LC_MESSAGES
	
%dir %{_datadir}/woeusb/locale/zh_TW
	
%dir %{_datadir}/woeusb/locale/zh_TW/LC_MESSAGES
	
%lang(fr) %{_datadir}/woeusb/locale/fr/LC_MESSAGES/woeusb.mo
	
%lang(fr) %{_datadir}/woeusb/locale/fr/LC_MESSAGES/wxstd.mo
	
%lang(zh) %{_datadir}/woeusb/locale/zh_TW/LC_MESSAGES/woeusb.mo
	
 
	
 
	
%changelog

* Sun Apr 14 2019 Josie Herzog 3.2.12

- Initial release
- Initial script provided by Matt Prahl <mprahl@redhat.com>

