# $Id: $
# Authority: dries
# Upstream: Michael Buesch <mbuesch@freenet.de>

# Screenshot: http://passwordmanager.sourceforge.net/1.png
# ScreenshotURL: http://passwordmanager.sourceforge.net/screenshots.html

%define real_version 1.0pre1

Summary: Personal password manager
Name: passwordmanager
Version: 1.0
Release: 0.pre1
License: GPL
Group: Applications/Productivity
URL: http://passwordmanager.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/passwordmanager/pwmanager-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel, libart_lgpl-devel, arts-devel, gcc-c++,
BuildRequires: gettext, XFree86-devel, zlib-devel, qt-devel, 
BuildRequires: libjpeg-devel, kdelibs-devel, bzip2-devel
%{?fc2:BuildRequires: libselinux-devel}

%description
PwManager saves your passwords blowfish-encrypted in one file, so you have
to remember only one master-password instead of all. Instead of the
master-password you can use a chipcard, so you don't have to remember a
password to access the list.

%prep
%setup -n pwmanager-%{real_version}

%build
%configure \
	--x-libraries="%{_prefix}/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS VERSION COPYING.LGPL AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/*
%{_datadir}/locale/*/LC_MESSAGES/pwmanager.mo
%{?fc2:%{_datadir}/services/kded/pwmanager_kwalletemu.desktop}
%{_datadir}/applnk/Applications/pwmanager.desktop
%{_datadir}/icons/*/*/apps/pw*.png
%{_datadir}/apps/pwmanager
%{?fc2:%{_libdir}/kde3/kded_pwmanager_kwalletemu.*}

%changelog
* Sun Jun 20 2004 Dries Verachtert <dries@ulyssis.org> - 1.0-pre1.1
- Update to version 1.0-pre1.

* Sat Jun 5 2004 Dries Verachtert <dries@ulyssis.org> - 0.8.1-1
- Update to version 0.8.1.

* Tue Jun 1 2004 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Initial package.
