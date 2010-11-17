# $Id$
# Authority: dag
# Upstream: Sean M. Burke <sburke$cpan,org>

### EL6 ships with perl-XML-TreeBuilder-3.09-16.1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-TreeBuilder

Summary: Perl module that implements a parser that builds a tree of XML::Element objects
Name: perl-XML-TreeBuilder
Version: 3.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-TreeBuilder/

Source: http://www.cpan.org/modules/by-module/XML/XML-TreeBuilder-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-XML-TreeBuilder is a Perl module that implements a parser
that builds a tree of XML::Element objects.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/XML::Element.3pm*
%doc %{_mandir}/man3/XML::TreeBuilder.3pm*
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/Element.pm
%{perl_vendorlib}/XML/TreeBuilder.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 3.09-1
- Initial package. (using DAR)
