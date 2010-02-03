# $Id$
# Upstream: Eric J. Roode <eric.roode.cpan@gmail.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name Iterator

Summary: A general-purpose iterator class
Name: perl-Iterator
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Iterator

Source: http://search.cpan.org/CPAN/authors/id/R/RO/ROODE/Iterator-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(Exception::Class) >= 1.21
BuildRequires: perl(Test::Simple) >= 0.40
Requires: perl(Exception::Class) >= 1.21
Requires: perl(Test::Simple) >= 0.40

%filter_from_requires /^perl*/d
%filter_setup

%description
This module is meant to be the definitive implementation of iterators, as popularized by Mark Jason Dominus's lectures and recent book (Higher Order Perl, Morgan Kauffman, 2005).

An "iterator" is an object, represented as a code block that generates the "next value" of a sequence, and generally implemented as a closure. When you need a value to operate on, you pull it from the iterator. If it depends on other iterators, it pulls values from them when it needs to. Iterators can be chained together (see Iterator::Util for functions that help you do just that), queueing up work to be done but not actually doing it until a value is needed at the front end of the chain. At that time, one data value is pulled through the chain.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} 

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Iterator.3pm*
%{perl_vendorlib}/Iterator.pm

%changelog
* Wed Feb 03 2010 Christoph Maser <cmr@financial.com> - 0.03-1
- initial package

