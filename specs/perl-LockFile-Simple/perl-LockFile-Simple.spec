# $Id$
# Authority: dries
# Upstream: Johan Vromans <jv$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name LockFile-Simple

Summary: Simple file locking
Name: perl-LockFile-Simple
Version: 0.207
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/LockFile-Simple/

Source: http://www.cpan.org/modules/by-module/LockFile/LockFile-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The LockFile::Simple extension provides simple file locking, of
the advisory kind, i.e. it requires cooperation between applications
wishing to lock the same files.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/LockFile::Simple.3pm*
%dir %{perl_vendorlib}/LockFile/
%{perl_vendorlib}/LockFile/Lock/
%{perl_vendorlib}/LockFile/Lock.pm
%{perl_vendorlib}/LockFile/Manager.pm
%{perl_vendorlib}/LockFile/Simple.pm

%changelog
* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 0.207-1
- Updated to release 0.207.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.206-1
- Updated to release 0.206.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.2.5-1
- Initial package.
