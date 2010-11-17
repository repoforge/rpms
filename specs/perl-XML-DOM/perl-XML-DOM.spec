# $Id$
# Authority: dag
# Upstream: T.J. Mather <tjmather$maxmind,com>

### EL6 ships with perl-XML-DOM-1.44-7.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-DOM

Summary: Perl module for building DOM Level 1 compliant document structures
Name: perl-XML-DOM
Version: 1.44
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-DOM/

Source: http://www.cpan.org/modules/by-module/XML/XML-DOM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a Perl extension to XML::Parser. It adds a new 'Style' to XML::Parser,
called 'Dom', that allows XML::Parser to build an Object Oriented datastructure
with a DOM Level 1 compliant interface.
For a description of the DOM (Document Object Model), see :
http://www.w3.org/DOM/

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

### Clean up docs
find samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS Changes FAQ.xml MANIFEST META.yml README samples/
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/DOM/
%{perl_vendorlib}/XML/DOM.pm
%dir %{perl_vendorlib}/XML/
%dir %{perl_vendorlib}/XML/Handler/
%{perl_vendorlib}/XML/Handler/BuildDOM.pm

%changelog
* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 1.44-2
- Disabled auto-requires for samples/.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.44-1
- Updated to release 1.44.

* Fri Dec 17 2004 Matthias Saou <http://freshrpms.net/> 1.43-1
- Initial package based on Dries' perl-XML-RegExp spec file.
