# $Id$
# Authority: dries
# Upstream: Carey Evans <careye$spamcop,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Sync

Summary: Access to fsync() and sync() function calls
Name: perl-File-Sync
Version: 0.09
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Sync/

Source: http://www.cpan.org/modules/by-module/File/File-Sync-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
It provides Perl interfaces to the Unix sync(2) and POSIX.1b fsync(2)
system calls. The fsync() call is needed for putting messages into
qmail maildirs, and sync() is included for completeness.

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
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/File/
%{perl_vendorarch}/File/Sync.pm
%dir %{perl_vendorarch}/auto/File/
%{perl_vendorarch}/auto/File/Sync/

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
