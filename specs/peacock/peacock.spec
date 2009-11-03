# $Id$

# Authority: dag

%define rev 2

Summary: WYSIWYG HTML Editor for Gnome
Name: peacock
Version: 1.9.1
Release: 0.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://peacock.sourceforge.net/

Source: http://dl.sf.net/peacock/peacock-%{version}.tar.gz
#Patch: peacock-1.9.1-rh.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: libgnomeui-devel >= 2.0.0
BuildRequires: libbonoboui-devel >= 2.0.0
BuildRequires: libglade2-devel >= 2.0.1
BuildRequires: gtksourceview-devel >= 0.5.0
BuildRequires: libgnomeprint22-devel >= 2.2.0

Requires:  gtkhtml3 >= 3.0

%description
Peacock is an HTML Editor for Gnome. Its is distributed under the GNU GPL License. Using the latest Gnome technologies like Bonobo, GtkHTML it hopes to provide the Web Developers a congenial environment for making Websites. Still in its nascent stages it support basic WYSIWYG HTML Editing and advanced editing operations.

#%package devel
#Summary: Libraries/include files for peacock
#Group: Development/Libraries
#Requires: %{name} = %{version}-%{release}

#%description devel
#Development headers for peacock.

%prep
%setup -q
#%patch -p1 -b .rh

%build
%configure
#		--prefix=%{_prefix} \
#		--bindir=%{_bindir} \
#		--datadir=%{_datadir}/%{name} \
#		--mandir=%{_mandir} \
#		--confdir=%{_sysconfdir}/%{name}

make

%install
%{__rm} -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT/

%makeinstall

# create a launcher icon
mkdir -p %{buildroot}%{_sysconfdir}/X11/applnk/Internet
cat > %{buildroot}%{_sysconfdir}/X11/applnk/Internet/peacock.desktop << EOF
[Desktop Entry]
Name=Peacock
Comment=%{summary}
Exec=%{name}-%{rev}
Icon=%{_datadir}/%{name}-%{rev}/pixmaps/peacock-logo.png
Terminal=0
Type=Application
EOF

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/%{name}-%{rev}
%{_datadir}/%{name}-%{rev}/*
#%{_datadir}/locale/*
%{_sysconfdir}/X11/applnk/Internet/peacock.desktop

#%files devel
#%defattr(-, root, root)
#%dir %{_includedir}/%{name}-%{version}
#%{_includedir}/%{name}-%{version}/*
#%{_libdir}/debug/usr/bin/%{name}-%{rev}.debug
#%{_prefix}/src/debug/%{name}-%{version}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.9.1-0.2
- Rebuild for Fedora Core 5.

* Tue Sep 09 2003 Gawain Lynch <gawain_lynch@yahoo.com> 1.9.1-1
- inital spec
