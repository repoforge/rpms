# $Id$

# Authority: dag

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: The Pan Newsreader
Name: pan
Version: 0.14.2.91
Release: 1
Epoch: 1
License: GPL
Group: Applications/Internet
URL: http://pan.rebelbase.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://pan.rebelbase.com/download/releases/%{version}/SOURCE/pan-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: glib2-devel >= 2.0.4, gtk2-devel >= 2.0.5, libxml2-devel >= 2.4.22
BuildRequires: gnet2-devel, gtkspell >= 2.0.2

%description
Pan is a newsreader, loosely based on Agent and Gravity, which attempts
to be pleasant to use for new and advanced users alike. It has all the
typical features found in newsreaders and also supports offline newsreading,
sophisticated filtering, multiple connections, and a number of extra features
for power users and alt.binaries fans. It's also the only Unix newsreader
to get a perfect score on the Good Net-Keeping Seal of Approval evalutions.

%prep
%setup

%build
%configure \
	--program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags} \
	LDFLAGS="-s"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%if %{dfi}
%else
desktop-file-install --vendor gnome --delete-original \
	--add-category X-Red-Hat-Base                 \
	--dir %{buildroot}%{_datadir}/applications    \
	%{buildroot}%{_datadir}/gnome/apps/Internet/*.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ANNOUNCE.html AUTHORS ChangeLog COPYING CREDITS INSTALL NEWS README TODO
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*

%changelog
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
