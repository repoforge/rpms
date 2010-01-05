# $Id$
# Authority: shuff
# Upstream: Claes Jakobsson <claes$surfar,nu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name JavaScript

Summary: Perl extension for executing embedded JavaScript
Name: perl-%{real_name}
Version: 1.15
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/JavaScript/

Source: http://search.cpan.org/CPAN/authors/id/C/CL/CLAESJAC/JavaScript-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
#BuildArch: noarch

BuildRequires: js-devel >= 1:1.7
BuildRequires: nspr-devel
BuildRequires: perl
BuildRequires: perl(Config)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Temp)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: js >= 1:1.7
Requires: perl


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Always thought JavaScript was for web-applications only? well, think again...

This modules gives you the power of embedded JavaScript in your Perl
applications. You can write your subroutines, classes and so forth in Perl and
make them callable from JavaScript. Variables such as primitive types, objects
and functions are automagically converted between the different environments.
If you return a JavaScript function you can call it as a normal code-reference
from Perl.

JavaScript is a great as an embedded language because it has no I/O, no IPC and
pretty much anything else that can interfer with the system. It's also an easy
yet powerful language that zillions of developers worldwide knows.

Note that this module is not a JavaScript compiler/interpreter written in Perl
but an interface to the SpiderMonkey engine used in the Mozilla-family of
browsers.

%prep
%setup -n %{real_name}-%{version}

%build
export JS_THREADSAFE=0 JS_UTF8=0 JS_ENABLE_E4X=1 
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
%doc Changes CREDITS MANIFEST META.yml README
%doc %{_mandir}/man?/*
%dir %{perl_vendorarch}/Test/
%{perl_vendorarch}/Test/*
%{perl_vendorarch}/JavaScript.pm
%{perl_vendorarch}/JavaScript/
%{perl_vendorarch}/auto/JavaScript/

%changelog
* Tue Jan  5 2010 Christoph Maser <cmr@financial.com> - 1.15-1
- Updated to version 1.15.

* Wed Dec 23 2009 Steve Huff <shuff@vecna.org> - 1.14-1
- Updated to version 1.14.

* Wed Nov 18 2009 Steve Huff <shuff@vecna.org> - 1.12-1
- Initial package.
