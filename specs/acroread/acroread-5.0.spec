# $Id: acroread.spec 2525 2004-11-20 17:41:43Z dag $
# Authority: dag


%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

%define real_version 5010

Summary: Adobe Reader for viewing PDF files
Name: acroread
Version: 5.0.10
Release: 1%{?dist}
License: Commercial, Freely Distributable
Group: Applications/Publishing
URL: http://www.adobe.com/products/acrobat/readermain.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ardownload.adobe.com/pub/adobe/acrobatreader/unix/5.x/linux-%{real_version}.tar.gz
Source1: acroread.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i386
BuildRequires: perl
%{?!_without_freedesktop:BuildRequires: desktop-file-utils}
Obsoletes: acrobat
Requires: htmlview

%description
Adobe Reader is part of the Adobe Acrobat family of software,
which lets you view, distribute, and print documents in Portable
Document Format (PDF)--regardless of the computer, operating system,
fonts, or application used to create the original file.

PDF files retain all the formatting, fonts, and graphics of the
original document, and virtually any PostScript(TM) document can
be converted into a PDF file. Adobe Acrobat Reader have a plug-in
for Netscape Navigator to to view PDF files inline

%package -n mozilla-acroread
Summary: Adobe Reader plug-in for viewing PDF files with the mozilla browser
Group: Applications/Internet
Requires: %{name} = %{version}
#Requires: %{_libdir}/mozilla/plugins/
Provides: acroread-plugin = %{version}-%{release}
Obsoletes: acroread-plugin < %{version}

%description -n mozilla-acroread
This package provides the Adobe Reader plugin for mozilla.

%prep
%setup -c

%{__cat} <<EOF >acroread.desktop
[Desktop Entry]
Name=Adobe Reader
Comment=View and print PDF files
Exec=acroread
Terminal=false
Type=Application
Icon=acroread.png
MimeType=application/pdf
Categories=Application;Graphics;
Encoding=UTF-8
EOF

%{__cat} <<EOF >WebLink
*LinkDisplay:	CTRL
*OpenURL:	NO
*IsMapped:	NO
*Progress:	NO
*Toolbar:	YES
*SelectedBrowser:	/usr/bin/htmlview	
*SelectedDriver:	Netscape
EOF

%build

%install
%{__rm} -rf %{buildroot}

%{__install} -d -m0755 %{buildroot}%{_libdir}/acroread/
%{__tar} -xvf installers/COMMON.TAR -C %{buildroot}%{_libdir}/acroread/
%{__tar} -xvf installers/LINUXRDR.TAR -C %{buildroot}%{_libdir}/acroread/

%{__mv} -f %{buildroot}%{_libdir}/acroread/bin/acroread.sh %{buildroot}%{_libdir}/acroread/bin/acroread

### Fixup path and fixed LANG/LC_ALL settings until Adobe adds Unicode locale support
%{__perl} -pi -e '
	s|^install_dir=.*$|install_dir=%{_libdir}/acroread/Reader\n
NLANG="\${LANG//.UTF-8/.ISO8859-1}"
export LANG="\${NLANG:-C}"
NLC_ALL="\${LC_ALL//.UTF-8/.ISO8859-1}"
export LC_ALL="\${NLC_ALL:-C}"
MALLOC_CHECK_=0
export MALLOC_CHECK_|;
	' %{buildroot}%{_libdir}/acroread/bin/acroread

### Shutup some rpm permission warnings
%{__chmod} +x %{buildroot}%{_libdir}/acroread/Reader/*/lib/lib*.so* %{buildroot}%{_libdir}/acroread/Browsers/*/*.so

%{__install} -D -m0644 WebLink %{buildroot}%{_libdir}/acroread/Reader/intellinux/app-defaults/WebLink

### Make links
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__ln_s} -f %{_libdir}/acroread/bin/acroread %{buildroot}%{_bindir}/acroread

%{__install} -d -m0755 %{buildroot}%{_prefix}/X11R6/%{_lib}/X11/app-defaults/
%{__ln_s} -f %{_libdir}/acroread/Reader/intellinux/app-defaults/AcroRead %{buildroot}%{_prefix}/X11R6/%{_lib}/X11/app-defaults/AcroRead
%{__ln_s} -f %{_libdir}/acroread/Reader/intellinux/app-defaults/WebLink %{buildroot}%{_prefix}/X11R6/%{_lib}/X11/app-defaults/WebLink

%{__install} -d -m0755 %{buildroot}%{_libdir}/netscape/plugins/
%{__ln_s} -f %{_libdir}/acroread/Browsers/intellinux/nppdf.so %{buildroot}%{_libdir}/netscape/plugins/nppdf.so

%{__install} -d -m0755 %{buildroot}%{_libdir}/mozilla/plugins/
%{__ln_s} -f %{_libdir}/acroread/Browsers/intellinux/nppdf.so %{buildroot}%{_libdir}/mozilla/plugins/nppdf.so

%{__install} -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/acroread.png

### Strip binaries and libraries
#%{__strip} %{buildroot}%{_libdir}/acroread/Reader/intellinux/bin/acroread %{buildroot}%{_libdir}/acroread/Reader/intellinux/lib/*.so.*

%if %{?_without_freedesktop:1}0
        %{__install} -D -m0644 acroread.desktop %{buildroot}%{_datadir}/gnome/apps/Graphics/acroread.desktop
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
        desktop-file-install --vendor %{desktop_vendor}    \
                --add-category X-Red-Hat-Base              \
                --dir %{buildroot}%{_datadir}/applications \
                acroread.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc installers/README installers/*.TXT 
%{_bindir}/acroread
%dir %{_libdir}/acroread/
%{_libdir}/acroread/Reader/
%{_libdir}/acroread/Resource/
%{_libdir}/acroread/bin/
%{_prefix}/X11R6/%{_lib}/X11/app-defaults/AcroRead
%{_prefix}/X11R6/%{_lib}/X11/app-defaults/WebLink
%{_datadir}/pixmaps/acroread.png
%{?_without_freedesktop:%{_datadir}/gnome/apps/Graphics/acroread.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-acroread.desktop}

%files -n mozilla-acroread
%defattr(-, root, root, 0755)
%dir %{_libdir}/acroread/
%{_libdir}/acroread/Browsers/
%{_libdir}/mozilla/plugins/nppdf.so
%{_libdir}/netscape/plugins/nppdf.so

%changelog
* Mon Dec 20 2004 Dag Wieers <dag@wieers.com> - 5.0.10-1
- Feedback from Jason L Tibbitts.
- Updated to release 5.0.10.

* Thu Nov 18 2004 Dag Wieers <dag@wieers.com> - 5.0.9-2
- Removed %%{_libdir}/mozilla/plugins/

* Thu Jun 24 2004 Dag Wieers <dag@wieers.com> - 5.0.9-1
- Updated to release 5.0.9.
- Fixed the acroread icon. (Sahak Petrosyan)
- Added fix for crash when doing 'Find' on non-existing strings. (Stefan Hoelldampf)

* Tue Jan 27 2004 Dag Wieers <dag@wieers.com> - 5.0.8-1
- Added fix to make locale settings still work. (Fernando Lozano)

* Mon Jan 26 2004 Dag Wieers <dag@wieers.com> - 5.0.8-0
- Added exports for LANG and LC_ALL, just in case. (Axel Thimm)
- Updated to release 5.0.8.

* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 5.0.7-2
- Fixed Unicode locale support, again. (Matthew Mastracci)

* Fri Aug 01 2003 Dag Wieers <dag@wieers.com> - 5.0.7-1
- Put mozilla plugins into a seperate package.
- Improved the desktop file.

* Sun Jul 13 2003 Dag Wieers <dag@wieers.com> - 5.0.7-0
- Initial package. (using DAR)
