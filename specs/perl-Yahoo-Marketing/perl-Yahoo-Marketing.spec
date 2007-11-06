# $Id$
# Authority: dries
# Upstream: Jeff Lavallee <jeff%20at%20zeroclue%20dot%20com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Yahoo-Marketing

Summary: Interface for Yahoo! Search Marketing's Web Services
Name: perl-Yahoo-Marketing
Version: 2.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Yahoo-Marketing/

Source: http://search.cpan.org//CPAN/authors/id/J/JL/JLAVALLEE/Yahoo-Marketing-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(SOAP::Lite), perl(Test::Class), perl(XML::XPath)
BuildRequires: perl(YAML)

%description
An interface for Yahoo! Search Marketing's Web Services.

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
%doc %{_mandir}/man3/Yahoo::Marketing*.3*
%dir %{perl_vendorlib}/Yahoo/
%{perl_vendorlib}/Yahoo/Marketing.pm
%{perl_vendorlib}/Yahoo/Marketing/

%changelog
* Sun Aug 12 2007 Dries Verachtert <dries@ulyssis.org> - 2.02-1
- Updated to release 2.02.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
