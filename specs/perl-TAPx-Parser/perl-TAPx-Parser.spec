# $Id$
# Authority: dries
# Upstream: Curtis &quot;Ovid&quot; Poe <ovid$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name TAPx-Parser

Summary: TAPx Parser
Name: perl-TAPx-Parser
Version: 0.30
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/TAPx-Parser/

Source: http://search.cpan.org//CPAN/authors/id/O/OV/OVID/TAPx-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
A parser for TAP output.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/TAPx/
%{perl_vendorlib}/TAPx/Parser.pm
%{perl_vendorlib}/TAPx/Parser/

%changelog
* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Initial package.
