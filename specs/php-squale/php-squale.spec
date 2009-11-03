# $Id$
# Authority: matthias

%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)

Summary: A module for PHP applications that use SQuaLe
Name: php-squale
Version: 0.1.10
Release: 0.1%{?dist}
License: GPL
Group: Development/Languages
URL: http://squale.sourceforge.net/
Source: http://dl.sf.net/squale/squale-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: php-common, squale >= %{version}
BuildRequires: php-devel, squale-devel >= %{version}
# We also need php for the eventual /etc/php.d directory
BuildRequires: php
# aclocal and autoconf required by phpize
BuildRequires: automake, autoconf, libtool

%description
A module for PHP applications that use SQuaLe.


%prep
%setup -n squale-%{version}


%build
pushd contrib/php
    test -x configure || phpize
    %configure
    %{__make} %{?_smp_mflags}
popd


%install
%{__rm} -rf %{buildroot}
pushd contrib/php
    %{__make} install INSTALL_ROOT=%{buildroot}
popd

# Drop in the bit of configuration
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.d
%{__cat} > %{buildroot}%{_sysconfdir}/php.d/squale.ini << 'EOF'
; Enable squale extension module
extension=squale.so
EOF


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc contrib/php/squale.php
%config %{_sysconfdir}/php.d/squale.ini
%{php_extdir}/squale.so


%changelog
* Tue Oct  3 2006 Matthias Saou <http://freshrpms.net/> 0.1.10-0.1
- Update to 0.1.10 pre-version.
- Don't require php but php-common instead, to work with fastcgi.

* Tue Sep 26 2006 Matthias Saou <http://freshrpms.net/> 0.1.9-1
- Update to 0.1.9.

* Mon Apr 24 2006 Matthias Saou <http://freshrpms.net/> 0.1.6-1
- Update to 0.1.6.
- Now use the full original squale source, it's easier to update.

* Wed Nov 16 2005 Matthias Saou <http://freshrpms.net/> 0.1.4-2
- Rebuild against PHP 4.4.1.

* Fri Apr 15 2005 Matthias Saou <http://freshrpms.net/> 0.1.4-1
- Update to 0.1.4.

* Tue Apr 12 2005 Matthias Saou <http://freshrpms.net/> 0.1.3-2
- Add php-squale-0.1.3-lib64.patch to fix lib64 detection.

* Thu Jan 20 2005 Matthias Saou <http://freshrpms.net/> 0.1.3-1
- Update to 0.1.3.

* Thu Oct 14 2004 Matthias Saou <http://freshrpms.net/> 0.0.7-1
- Update to 0.0.7.

* Mon May 10 2004 Matthias Saou <http://freshrpms.net/> 0.0.3-1
- Update to 0.0.3.
- Disable %{phpize} if configure is found (4.1.x build phpized with 4.3.x).

* Fri Mar 26 2004 Matthias Saou <http://freshrpms.net/> 0.0.1-1
- Initial RPM release.

