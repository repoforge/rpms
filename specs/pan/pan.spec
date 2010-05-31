# $Id: pan.spec 4308 2006-04-21 22:20:20Z dries $
# Authority: dag
# Upstream: <pan-devel$nongnu,org>

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: The Pan Newsreader
Name: pan
Version: 0.133
Release: 1%{?dist}
Epoch: 1
License: GPL
Group: Applications/Internet
URL: http://pan.rebelbase.com/

Source: http://pan.rebelbase.com/download/releases/%{version}/source/pan-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel >= 2.0.4
BuildRequires: gmime-devel >= 2.1.9
BuildRequires: gnet2-devel
BuildRequires: gtk2-devel >= 2.0.5
BuildRequires: gtkspell-devel >= 2.0.2
BuildRequires: libxml2-devel >= 2.4.22
BuildRequires: pcre-devel >= 5.0, gettext
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
Pan is a newsreader, loosely based on Agent and Gravity, which attempts
to be pleasant to use for new and advanced users alike. It has all the
typical features found in newsreaders and also supports offline newsreading,
sophisticated filtering, multiple connections, and a number of extra features
for power users and alt.binaries fans. It's also the only Unix newsreader
to get a perfect score on the Good Net-Keeping Seal of Approval evalutions.

%prep
%setup

%{__perl} -pi.orig -e 's|StartupNotify=false|StartupNotify=true|' pan.desktop.in

%build
%configure \
    --program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags} LDFLAGS="-s"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%if %{!?_without_freedesktop:1}0
desktop-file-install --vendor %{desktop_vendor} \
    --delete-original                           \
    --add-category Application                  \
    --add-category Network                      \
    --add-category X-Red-Hat-Base               \
    --dir %{buildroot}%{_datadir}/applications  \
    %{buildroot}%{_datadir}/applications/pan.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/pan
%{_datadir}/applications/%{desktop_vendor}-pan.desktop
%{_datadir}/pixmaps/pan.png

%changelog
* Wed Dec 31 2008 Dag Wieers <dag@wieers.com> - 0.133-1
- Updated to release 0.133.

* Tue Jun 10 2008 Dag Wieers <dag@wieers.com> - 0.132-2
- Added patch from Fedora.

* Thu Mar 13 2008 Heiko Adams <info-2007@fedora-blog.de> - 0.132-1
- Updated to release 0.132.

* Sat Jun 16 2007 Dag Wieers <dag@wieers.com> - 0.131-1
- Updated to release 0.131.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 0.129-1
- Updated to release 0.129.

* Wed Mar 21 2007 Dag Wieers <dag@wieers.com> - 0.125-1
- Updated to release 0.125.

* Tue Mar 30 2004 Dag Wieers <dag@wieers.com> - 0.14.2.91-2
- Fixed missing categories in desktop-file. (Neil Bird)

* Sun Mar 28 2004 Dag Wieers <dag@wieers.com> - 0.14.2.91-1
- Updated to release 0.14.2.91.

* Mon Sep 08 2003 Dag Wieers <dag@wieers.com> - 0.14.2-1
- Build against gnet2-devel.

* Thu Sep 04 2003 Dag Wieers <dag@wieers.com> - 0.14.2-0
- Updated to release 0.14.2.

* Sat Aug 30 2003 Dag Wieers <dag@wieers.com> - 0.14.1-0
- Updated to release 0.14.1.

* Sat Aug 16 2003 Dag Wieers <dag@wieers.com> - 0.14.0.95-0
- Updated to release 0.14.0.95.

* Thu Jul 31 2003 Dag Wieers <dag@wieers.com> - 0.14.0.93-0
- Updated to release 0.14.0.93.

* Sun Jul 27 2003 Dag Wieers <dag@wieers.com> - 0.14.0.92-0
- Updated to release 0.14.0.92.

* Fri Jul 18 2003 Dag Wieers <dag@wieers.com> - 0.14.0.91-0
- Updated to release 0.14.0.91.

* Wed Jul 09 2003 Dag Wieers <dag@wieers.com> - 0.14.0.90-0
- Updated to release 0.14.0.90.

* Wed May 07 2003 Dag Wieers <dag@wieers.com> - 0.14.0-0
- Updated to release 0.14.0.

* Sun Apr 27 2003 Dag Wieers <dag@wieers.com> - 0.13.96-0
- Updated to release 0.13.96.

* Tue Apr 22 2003 Dag Wieers <dag@wieers.com> - 0.13.95-0
- Updated to release 0.13.95.

* Wed Apr 16 2003 Dag Wieers <dag@wieers.com> - 0.13.94-0
- Updated to release 0.13.94.

* Wed Apr 02 2003 Dag Wieers <dag@wieers.com> - 0.13.93-0
- Updated to release 0.13.93.

* Sat Mar 15 2003 Dag Wieers <dag@wieers.com> - 0.13.91-0
- Updated to release 0.13.91.

* Thu Mar 13 2003 Dag Wieers <dag@wieers.com> - 0.13.90-0
- Updated to release 0.13.90.

* Fri Feb 28 2003 Dag Wieers <dag@wieers.com> - 0.13.4-0
- Initial package. (using DAR)
