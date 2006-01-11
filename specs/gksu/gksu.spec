# $Id$
# Authority: dries
# Upstream: Gustavo Noronha <kov$debian,org>

# Screenshot: http://www.nongnu.org/gksu/gksu2.png

Summary: Graphical frontend to su
Name: gksu
Version: 1.3.4
Release: 1
License: GPL
Group: Applications/
URL: http://www.nongnu.org/gksu/

Source: http://people.debian.org/~kov/gksu/gksu/gksu-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgksu-devel, gcc-c++, gettext, intltool, perl(XML::Parser)
BuildRequires: bison, gtk-doc

%description
Gtk+ frontend to /bin/su. It supports login shells and preserving environment 
when acting as a su frontend. It is useful to menu items or other graphical 
programs that need to ask a user's password to run another program as another 
user.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/*
%{_sysconfdir}/gconf/schemas/gksu.schemas
%{_bindir}/gksu*
%{_datadir}/gksu/
%{_datadir}/pixmaps/gksu**.png
%{_datadir}/applications/gksu*.desktop

%changelog
* Sat Sep 17 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.4-1
- Initial package.
