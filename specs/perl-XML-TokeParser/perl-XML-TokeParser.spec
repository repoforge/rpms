# $Id$
# Authority: dag
# Upstream: D. H. <crazyinsomniac$yahoo,com>

### EL6 ships with perl-XML-TokeParser-0.05-2.1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-TokeParser

Summary: Perl module that implements a simplified interface to XML::Parser
Name: perl-XML-TokeParser
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-TokeParser/

Source: http://www.cpan.org/modules/by-module/XML/XML-TokeParser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-XML-TokeParser is a Perl module that implements a simplified
interface to XML::Parser.

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
%doc Changes MANIFEST META.yml README TODO
%doc %{_mandir}/man3/XML::TokeParser.3pm*
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/TokeParser.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
