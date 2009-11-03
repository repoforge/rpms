# $Id$
# Authority: dries
# Upstream: David Boyce <dsb$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IPC-ChildSafe

Summary: Control a child process without blocking
Name: perl-IPC-ChildSafe
Version: 3.16
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IPC-ChildSafe/

Source: http://www.cpan.org/modules/by-module/IPC/IPC-ChildSafe-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This distribution contains a C API for controlling a co-process as well
as a Perl module which drives the C API.  It's not necessary to use
the Perl wrapper; the C API can be called directly from C code if you
prefer. But generally it can be thought of as a Perl module with an XS
back end.

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
%dir %{perl_vendorarch}/IPC/
%{perl_vendorarch}/IPC/ChildSafe.pm
%{perl_vendorarch}/IPC/ClearTool.pm
%dir %{perl_vendorarch}/auto/IPC/
%{perl_vendorarch}/auto/IPC/ChildSafe

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 3.16-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 3.16-1
- Initial package.
