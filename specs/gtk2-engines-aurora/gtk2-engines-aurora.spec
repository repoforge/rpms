Name:           gtk2-engines-aurora
Version:        1.4
Packager:       Christopher Bratusek <nano-master@gmx.de>
Release:        2%{?dist}
License:        GPL-2
Source0:        aurora-%{version}.tar.gz
Source10:       gtkrc_themes.tar.bz2
Patch0:		76134-01_aurora_no_mbar_shadow.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  make, bash, gtk2-devel, sed
Group: 		System Environment/Libraries
URL: 		http://gnome-look.org/content/show.php/Aurora+Gtk+Engine?content=56438
Summary:        GTK+2 Theme Engine

%description
Aurora GTK+2 Theme Engine with Animation support

%prep
%setup -q -n aurora-%{version}
%patch0 -p0 -b .patch

%build
#cp config_sub.new config.sub
#cp config_guess.new config.guess
%configure --prefix=/usr --enable-animation
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/themes
(cd $RPM_BUILD_ROOT/%{_datadir}/themes;
bzcat %{SOURCE10} | tar -xvf -;)

#remove .la files
find $RPM_BUILD_ROOT -name *.la | xargs rm -f || true
#fix permission
find $RPM_BUILD_ROOT/%{_datadir}/themes -type f | xargs chmod 0644 || true

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog NEWS COPYING
%{_libdir}/gtk-2.0/*/engines/*
%{_datadir}/*

%changelog
* Mon Mar 03 2008 Heiko Adams <info-2007@fedora-blog.de> - 1.4-2
- added patch for "GtkMenuBar::shadow_type = GTK_SHADOW_NONE does not work" problem

* Mon Jan 14 2008 Heiko Adams <info-2007@fedora-blog.de> - 1.4-1
- version update to 1.4

* Mon Nov 19 2007 Heiko Adams <info@fedora-blog.de> - 1.3-13.2
- Rebuild for rpmforge
