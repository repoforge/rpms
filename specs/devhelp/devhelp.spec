# $Id$

# Authority: dag
# Upstream: Mikael Hallendal <micke@imendio.com>

Summary: API document browser
Name: devhelp
Version: 0.9
Release: 0
Group: Development/Tools
License: GPL
URL: http://www.imendio.com/projects/devhelp/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.gnome.org/pub/GNOME/sources/devhelp/0.9/devhelp-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gtk2-devel >= 2.3.1, libgnomeui-devel >= 2.2, gnome-vfs2-devel >= 2.2
BuildRequires: gtkhtml2-devel >= 2.0.0, intltool

%description
devhelp is an API document browser for GNOME.

%prep
%setup

%build
intltoolize
%configure \
	--with-html-widget="gtkhtml2"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/devhelp/*.a \
		%{buildroot}%{_libdir}/devhelp/*.la

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
#%{_libdir}/devhelp/
%{_datadir}/devhelp/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{_datadir}/mime-info/*

%changelog
* Wed Mar 17 2004 Dag Wieers <dag@wieers.com> - 0.9-0
- Updated to release 0.9.

* Mon Feb 16 2004 Dag Wieers <dag@wieers.com> - 0.8.1-0
- Updated to release 0.8.1.

* Sun Jun 29 2003 Dag Wieers <dag@wieers.com> - 0.7-0
- Updated to release 0.7.

* Sun Apr 27 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Initial package. (using DAR)
