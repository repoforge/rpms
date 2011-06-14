# $Id:$
# Authority: shuff
# Upstream: Marc Lehmann <schmorp@schmorp.de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Async-Interrupt

Summary: Allow C/XS libraries to interrupt Perl asynchronously
Name: perl-Async-Interrupt
Version: 1.05
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Async-Interrupt/

Source: http://www.cpan.org/authors/id/M/ML/MLEHMANN/Async-Interrupt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(common::sense)
Requires: perl
Requires: perl(common::sense)

%filter_from_requires /^perl*/d
%filter_setup

%description
This module implements a single feature only of interest to advanced perl
modules, namely asynchronous interruptions (think "UNIX signals", which are
very similar).

Sometimes, modules wish to run code asynchronously (in another thread, or from
a signal handler), and then signal the perl interpreter on certain events. One
common way is to write some data to a pipe and use an event handling toolkit to
watch for I/O events. Another way is to send a signal. Those methods are slow,
and in the case of a pipe, also not asynchronous - it won't interrupt a running
perl interpreter.

This module implements asynchronous notifications that enable you to signal
running perl code from another thread, asynchronously, and sometimes even
without using a single syscall.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

# fix for stupid strip issue
%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes MANIFEST META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorarch}/auto/Async/Interrupt/*
%{perl_vendorarch}/Async/Interrupt.pm

%changelog
* Tue Jun 14 2011 Steve Huff <shuff@vecna.org> - 1.05-1
- Initial package.

