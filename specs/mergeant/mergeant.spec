# $Id$

# Authority: dag

# Upstream: Jorge Ferrer <jferrer@ieeesb.etsit.upm.es>

Summary: database administration tool
Name: mergeant
Version: 0.12.1
Release: 0
License: GPL
Group: Applications/Databases
URL: http://www.gnome-db.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.gnome-db.org/pub/gnome-db/sources/v%{version}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: libgda-devel, libgnomedb-devel
BuildRequires: scrollkeeper

Requires(post): scrollkeeper

%description
Mergeant is a database admin tool working with libgnomedb and libgda.

%prep
%setup

%build
%configure
### FIXME: Set proper MERGEANT_Helpdir, Applicationsdir and Pixmapdir in Makefiles
%{__perl} -pi.orig -e '
		s| = /usr/share/| = \$(datadir)/|;
		s| = /usr/lib/| = \$(libdir)/|;
	' Makefile */Makefile doc/*/Makefile
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO examples/ 
%doc %{_datadir}/gnome/help/mergeant/
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/applications/*.desktop
%{_datadir}/application-registry/*.applications
%{_datadir}/mime-info/*
%{_datadir}/mergeant/
%{_datadir}/pixmaps/*
%{_datadir}/omf/mergeant/

%changelog
* Fri Jun 13 2003 Dag Wieers <dag@wieers.com> - 0.12.1
- Initial package. (using DAR)
