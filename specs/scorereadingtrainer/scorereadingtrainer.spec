# $Id$

# Authority: dries
# Screenshot: http://scret.sourceforge.net/shot1.png
# ScreenshotURL: http://scret.sourceforge.net/

%define real_name ScoreReadingTrainer

%{?dtag: %{expand: %%define %dtag 1}}

Summary: musical score reading trainer
Name: scorereadingtrainer
Version: 0.1.3
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://scret.sourceforge.net/

Source: http://dl.sf.net/scret/ScoreReadingTrainer-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++
BuildRequires: qt-devel, fam-devel
%{?fc3:BuildRequires:libselinux-devel}
%{?fc2:BuildRequires:libselinux-devel}

%description
Score Reading Trainer helps you improve your (musical) score reading skills
by practicing with random scores. It shows you a random score and you have
to press the matching note for it.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup -n %{real_name}-%{version}

%build
source /etc/profile.d/qt.sh
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
%{?fc1:for i in $(find . -type f | egrep '\.ui'); do sed -i 's/version="3.."/version="3.1"/g;' $i; done}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source /etc/profile.d/qt.sh
echo RPM_BUILD_ROOT is $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
%{__make} install-strip
%find_lang %{real_name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/ScoreReadingTrainer
%{_datadir}/applnk/Edutainment/Miscellaneous/ScoreReadingTrainer.desktop
%{_datadir}/apps/ScoreReadingTrainer
%{_datadir}/doc/HTML/en/ScoreReadingTrainer
%{_datadir}/icons/*/*/apps/ScoreReadingTrainer.png


%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.3-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Sat May 27 2004 Dries Verachtert <dries@ulyssis.org> 0.1.3-1
- update to version 0.1.3

* Wed Feb 3 2004 Dries Verachtert <dries@ulyssis.org> 0.1.2-1
- update to version 0.1.2

* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 0.1.0-1
- first packaging for Fedora Core 1
