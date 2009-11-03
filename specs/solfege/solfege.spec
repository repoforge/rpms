# $Id$
# Authority: dag

Summary: Eartaining program for GNOME
Name: solfege
Version: 2.2.2
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://solfege.sourceforge.net/

Source: http://dl.sf.net/solfege/solfege-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: swig, texinfo, python >= 2.1, pygtk2 >= 0.6.3, gcc-c++
BuildRequires: pkgconfig, python-devel, m4, gettext, lilypond
Requires: pygnome >= 2.1, pygtk2 >= 0.6.3

%description
Solfege is an eartraining program for X written in python, using the
GTK+ and GNOME libraries. This is a development release, things might
be broken. See INSTALL file if you have problems running or installing
Solfege.

Eartraining is a big subject with many connections to music theory and
performance of music, so I won't even try to make "a complete
computerbased eartraining course". But I hope someone find this
software useful.

%prep
%setup

%build
%configure --with-gtkhtml
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall nopycompile="YES"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc changelog README TODO
%config %{_sysconfdir}/solfege1.4/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.2-1.2
- Rebuild for Fedora Core 5.

* Tue Mar 22 2005 Dag Wieers <dag@wieers.com> - 2.2.2-1
- Updated to release 2.2.2.

* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 2.1.0-1
- Updated to release 2.1.0.

* Mon Feb 10 2003 Dag Wieers <dag@wieers.com> - 1.4.10
- Initial package. (using DAR)
