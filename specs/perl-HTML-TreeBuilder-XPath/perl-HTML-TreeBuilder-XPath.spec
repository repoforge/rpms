# $Id$
# Authority: dries
# Upstream: Michel Rodriguez <mirod$xmltwig,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-TreeBuilder-XPath

Summary: XPath support for HTML::TreeBuilder
Name: perl-HTML-TreeBuilder-XPath
Version: 0.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-TreeBuilder-XPath/

Source: http://search.cpan.org//CPAN/authors/id/M/MI/MIROD/HTML-TreeBuilder-XPath-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
XPath support for HTML::TreeBuilder.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/HTML::TreeBuilder::XPath*
%{perl_vendorlib}/HTML/TreeBuilder/XPath.pm
%dir %{perl_vendorlib}/HTML/TreeBuilder/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
