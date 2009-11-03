# $Id$
# Authority: dries
# Upstream: Mark Morgan <makk384$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-XML-Parser

Summary: Parse an XML message into a user-defined class structure
Name: perl-Class-XML-Parser
Version: 0.901
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-XML-Parser/

Source: http://www.cpan.org/modules/by-module/Class/Class-XML-Parser-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Parse an XML message into a user-defined class structure.

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
%doc MANIFEST README
%doc %{_mandir}/man3/Class::XML::Parser.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/XML/
#%{perl_vendorlib}/Class/XML/Parser/
%{perl_vendorlib}/Class/XML/Parser.pm

%changelog
* Wed Nov 07 2007 Dag Wieers <dag@wieers.com> - 0.901-1
- Updated to release 0.901.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Initial package.
