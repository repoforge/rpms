# $Id$

# Authority: dries

# Todo: replace .desktop file by a freedesktop compliant one

Summary: musical score reading trainer
Name: scorereadingtrainer
Version: 0.1.2
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://scret.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/scret/ScoreReadingTrainer-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel, qt-devel
%{?fc2:BuildRequires:libselinux-devel}
Requires: kdelibs

# Screenshot: http://scret.sourceforge.net/shot1.png
# ScreenshotURL: http://scret.sourceforge.net/

%description
Score Reading Trainer helps you improve your (musical) score reading skills
by practicing with random scores. It shows you a random score and you have
to press the matching note for it.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup -n ScoreReadingTrainer-0.1.2

%build
. /etc/profile.d/qt.sh
%configure
%{?fc1:for i in $(find . -type f | egrep '\.ui'); do sed -i 's/version="3.."/version="3.1"/g;' $i; done}
%{__make} %{?_smp_mflags}

%install
. /etc/profile.d/qt.sh
echo RPM_BUILD_ROOT is $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
%{__make} install-strip

%files
%defattr(-,root,root,0755)
%doc README
%{_bindir}/ScoreReadingTrainer
/usr/share/applnk/Edutainment/Miscellaneous/ScoreReadingTrainer.desktop
/usr/share/apps/ScoreReadingTrainer/ScoreReadingTrainerui.rc
/usr/share/apps/ScoreReadingTrainer
/usr/share/doc/HTML/en/ScoreReadingTrainer
/usr/share/icons/*/*/apps/ScoreReadingTrainer.png
/usr/share/locale/*/LC_MESSAGES/ScoreReadingTrainer.mo


%changelog
* Wed Feb 3 2004 Dries Verachtert <dries@ulyssis.org> 0.1.2-1
- update to version 0.1.2

* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 0.1.0-1
- first packaging for Fedora Core 1
