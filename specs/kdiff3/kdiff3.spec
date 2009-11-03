# $Id$
# Authority: dries
# Upstream: Joachim Eibl <joachim,eibl$gmx,de>

Summary: Compares files or directories
Name: kdiff3
Version: 0.9.92
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://kdiff3.sourceforge.net/

Source: http://dl.sf.net/kdiff3/kdiff3-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gettext, kdelibs-devel, kdebase-devel

%description
KDiff3 is a program that compares two or three text input files or 
directories, shows the differences line by line and character by 
character, provides an automatic merge facility and an integrated 
editor for comfortable solving of merge conflicts, and has an 
intuitive graphical user interface.

%prep
%setup
# avoid buildproblem on rhel4 because of undefined entity
%{__perl} -pi -e 's|&Sander.Koning;||g; s|&vertaling.sander;||g;' doc/nl/index.docbook

%build
%configure --with-qt-libraries=$QTDIR/lib
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/kdiff3.1*
%{_bindir}/kdiff3
%{_libdir}/kde3/libkdiff3part.*
%{_libdir}/kde3/libkdiff3plugin.*
%{_datadir}/applnk/Development/kdiff3.desktop
%{_datadir}/applnk/.hidden/kdiff3plugin.desktop
%{_datadir}/apps/kdiff3/
%{_datadir}/apps/kdiff3part/
%{_datadir}/services/kdiff3*.desktop
%{_datadir}/icons/*/*/apps/kdiff3.png
%{_docdir}/HTML/*/kdiff3/
%{_docdir}/HTML/kdiff3/

%changelog
* Mon Aug 06 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.92-1
- Initial package.
