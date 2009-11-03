# $Id$
# Authority: dag

### Prevent the plugins from being stripped and disabled
%define __spec_install_post /usr/lib/rpm/brp-compress || :

# Don't create a debuginfo package.
%define debug_package %{nil}


%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Adobe Reader for viewing PDF files
Name: acroread
Version: 7.0.9
Release: 1%{?dist}
License: Commercial, Freely Distributable
Group: Applications/Publishing
URL: http://www.adobe.com/products/acrobat/readermain.html

Source: http://ardownload.adobe.com/pub/adobe/reader/unix/7x/%{version}/enu/AdobeReader_enu-%{version}-1.i386.tar.gz
NoSource: 0
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i386
BuildRequires: perl
%{?!_without_freedesktop:BuildRequires: desktop-file-utils}
Obsoletes: acrobat <= %{version}, AdobeReader_enu <= %{version}
Requires: htmlview

### Missing provides ?
Provides: libACE.so, libACE.so(VERSION), libAGM.so, libAGM.so(VERSION)
Provides: libBIB.so, libBIB.so(VERSION), libCoolType.so, libCoolType.so(VERSION)
Provides: libResAccess.so

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

%build

%install
%{__rm} -rf %{buildroot}

%{__install} -d -m0755 %{buildroot}%{_libdir}/acroread/
%{__tar} -xvf AdobeReader/COMMON.TAR -C %{buildroot}%{_libdir}/acroread/
%{__tar} -xvf AdobeReader/ILINXR.TAR -C %{buildroot}%{_libdir}/acroread/

### Silent some rpm permission warnings
#%{__chmod} +x %{buildroot}%{_libdir}/acroread/Reader/*/lib/lib*.so*

### Make links
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__ln_s} -f %{_libdir}/acroread/bin/acroread %{buildroot}%{_bindir}/acroread

### Need to hardlink, softlinks do not work
%{__install} -d -m0755 %{buildroot}%{_libdir}/netscape/plugins/
ln -f %{buildroot}%{_libdir}/acroread/Browser/intellinux/nppdf.so %{buildroot}%{_libdir}/netscape/plugins/nppdf.so
%{__install} -d -m0755 %{buildroot}%{_libdir}/mozilla/plugins/
ln -f %{buildroot}%{_libdir}/acroread/Browser/intellinux/nppdf.so %{buildroot}%{_libdir}/mozilla/plugins/nppdf.so

### Strip binaries and libraries
#%{__strip} %{buildroot}%{_libdir}/acroread/Reader/intellinux/bin/acroread %{buildroot}%{_libdir}/acroread/Reader/intellinux/lib/*.so.*

%{__install} -Dp -m0644 %{buildroot}%{_libdir}/acroread/Resource/Icons/AdobeReader.png %{buildroot}%{_datadir}/pixmaps/AdobeReader.png

%{__cp} -afp %{buildroot}%{_libdir}/acroread/Resource/Support/AdobeReader_GNOME.desktop acroread.desktop
%if %{?_without_freedesktop:1}0
        %{__install} -Dp -m0644 acroread.desktop %{buildroot}%{_datadir}/gnome/apps/Applications/acroread.desktop
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
%doc AdobeReader/*.htm AdobeReader/*.TXT
%{_bindir}/acroread
%dir %{_libdir}/acroread/
%{_libdir}/acroread/Reader/
%{_libdir}/acroread/Resource/
%{_libdir}/acroread/bin/
%{_datadir}/pixmaps/AdobeReader.png
%{?_without_freedesktop:%{_datadir}/gnome/apps/Applications/acroread.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-acroread.desktop}

%files -n mozilla-acroread
%defattr(-, root, root, 0755)
%dir %{_libdir}/acroread/
%{_libdir}/acroread/Browser/
%{_libdir}/mozilla/plugins/nppdf.so
%{_libdir}/netscape/plugins/nppdf.so

%changelog
* Thu Jan 11 2007 Dag Wieers <dag@wieers.com> - 7.0.9-1
- Updated to release 7.0.9.

* Mon Jun 12 2006 Dag Wieers <dag@wieers.com> - 7.0.8-1
- Updated to release 7.0.8.

* Sat Mar 04 2006 Dries Verachtert <dries@ulyssis.org> - 7.0.5-2
- Disabled creation of a debuginfo package.

* Fri Jan 27 2006 Dag Wieers <dag@wieers.com> - 7.0.5-1
- Updated to release 7.0.5.

* Fri Mar 18 2005 Dag Wieers <dag@wieers.com> - 7.0.0-2
- Disabled stripping globally to make plugin working. (Jürgen Möllenhoff)

* Tue Mar 15 2005 Dag Wieers <dag@wieers.com> - 7.0.0-1
- Updated to release 7.0.0.

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
