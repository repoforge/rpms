# $Id$
# Authority: dag
# Upstream: <pan-devel$nongnu,org>


%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: The Pan Newsreader
Name: pan
Version: 0.14.2.91
Release: 2%{?dist}
Epoch: 1
License: GPL
Group: Applications/Internet
URL: http://pan.rebelbase.com/

Source: http://pan.rebelbase.com/download/releases/%{version}/SOURCE/pan-%{version}.tar.bz2
Patch0: pan-0.14.2-gcc4.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel >= 2.0.4, gtk2-devel >= 2.0.5, libxml2-devel >= 2.4.22
BuildRequires: gnet2-devel, gtkspell-devel >= 2.0.2, gettext, pcre-devel >= 4.0
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
%patch0 -p1

%build
%configure \
	--program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags} LDFLAGS="-s"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%if %{!?_without_freedesktop:1}0
desktop-file-install --vendor %{desktop_vendor}    \
	--delete-original                          \
	--add-category Application                 \
	--add-category Network                     \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/gnome/apps/Internet/pan.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ANNOUNCE.html AUTHORS ChangeLog COPYING CREDITS INSTALL NEWS README TODO
%{_bindir}/pan
%{?_without_freedesktop:%{_datadir}/gnome/apps/Internet/pan.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-pan.desktop}
%{_datadir}/pixmaps/pan.png

%changelog
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
