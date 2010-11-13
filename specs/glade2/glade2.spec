# $Id$
# Authority: dag
# Rationale: This package doesn't need a lot of devel-packages.

### EL5 ships with glade2-2.12.1-6.el5
### EL4 ships with glade2-2.6.0-1
### EL3 ships with glade2-2.0.0-1
# ExclusiveDist: el2

%define real_name glade

Summary: GTK+ GUI builder
Name: glade2
Version: 2.0.1
Release: 0.2%{?dist}
License: GPL
Group: Development/Tools
URL: http://glade.gnome.org/

Source: ftp://ftp.gnome.org/pub/GNOME/pre-gnome2/sources/glade/glade-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gail-devel >= 0.17
BuildRequires: glib2-devel >= 2.2.0
BuildRequires: pango-devel >= 1.2.0
BuildRequires: gtk2-devel >= 2.2.0
BuildRequires: libgnomeui-devel >= 2.2.0
BuildRequires: libbonobo-devel >= 2.2.0
BuildRequires: libbonoboui-devel >= 2.2.0
BuildRequires: gnome-vfs2-devel >= 2.0.0
BuildRequires: bonobo-activation-devel >= 1.0.0
BuildRequires: libgnomecanvas-devel >= 2.0.0
BuildRequires: libgnomeprint22-devel >= 2.2.0
BuildRequires: libgnomeprintui22-devel >= 2.2.0
BuildRequires: desktop-file-utils >= 0.2.90
BuildRequires: scrollkeeper

Requires(post): scrollkeeper

%description
Glade is a free user interface builder for GTK+ and the GNOME GUI
desktop. Glade can produce C source code. Support for C++, Ada95,
Python, and Perl is also available, via external tools which process
the XML interface description files output by GLADE.

The glade2 package contains a version of Glade for GTK+ 2.0.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{real_name}-2.0

%if %{?fc1:1}%{!?fc1:0}
desktop-file-install --vendor gnome --delete-original \
	--add-category X-Red-Hat-Base                 \
	--dir %{buildroot}%{_datadir}/applications    \
	%{buildroot}%{_datadir}/applications/*.desktop
%endif

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_localstatedir}/scrollkeeper

%post
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}-2.0.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_datadir}/gnome/help/glade-2/
%{_datadir}/glade-2/
%{_datadir}/omf/glade-2/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/glade-2/
%{_datadir}/pixmaps/*.png
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.1-0.2
- Rebuild for Fedora Core 5.

* Thu Nov 23 2003 Dag Wieers <dag@wieers.com> - 2.0.1-0
- Updated to release 2.0.1.

* Sun Aug 17 2003 Dag Wieers <dag@wieers.com> - 2.0.0-2.0
- Initial package. (using DAR)
