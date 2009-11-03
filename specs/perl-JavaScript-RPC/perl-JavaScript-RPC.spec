# $Id$
# Authority: dries
# Upstream: Brian Cassidy <bricas$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name JavaScript-RPC

Summary: Remote procedure calls from JavaScript
Name: perl-JavaScript-RPC
Version: 0.3
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/JavaScript-RPC/

Source: http://www.cpan.org/modules/by-module/JavaScript/JavaScript-RPC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Remote procedure calls from JavaScript.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

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
%doc %{_mandir}/man3/JavaScript::RPC*
%{perl_vendorlib}/JavaScript/RPC.pm
%{perl_vendorlib}/JavaScript/RPC/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Initial package.
