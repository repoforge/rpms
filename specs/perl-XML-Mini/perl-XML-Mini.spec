# $Id$
# Authority: dries
# Upstream: Pat Deegan <pause$psychogenic,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Mini

Summary: MiniXML XML generator and parser interface
Name: perl-XML-Mini
Version: 1.38
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Mini/

Source: http://www.cpan.org/modules/by-module/XML/XML-Mini-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
XML::Mini is a set of Perl (and PHP) classes that allow you to access
XML data and create valid XML output with a tree-based hierarchy of
elements.

It provides an easy, object-oriented interface for manipulating XML
documents and their elements. It is currently being used to send
requests and understand responses from remote servers in Perl or PHP
applications.

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
%doc Changes INSTALL LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/XML::Mini.3pm*
%doc %{_mandir}/man3/XML::Mini::*.3pm*
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/Mini/
%{perl_vendorlib}/XML/Mini.pm

%changelog
* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 1.38-1
- Updated to release 1.38.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.8-1
- Initial package.
