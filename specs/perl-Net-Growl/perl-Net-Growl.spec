# $Id$
# Authority: shuff
# Upstream: Nathan McFarland <nmcfarl$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Growl

Summary: Growl Notifications over the network
Name: perl-%{real_name}
Version: 0.99
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Growl/

Source: http://search.cpan.org/CPAN/authors/id/N/NM/NMCFARL/Net-Growl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::Socket)
BuildRequires: perl(strict)
BuildRequires: perl(Test::More)
BuildRequires: perl(warnings)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Carp)
Requires: perl(Exporter)
Requires: perl(IO::Socket)
Requires: perl(strict)
Requires: perl(warnings)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
A simple interface to send Mac OS X Growl notifications across the network.
Growl only needs to be installed on the receiving Mac not on the machine using
this module.

To use register your app using 'register', send using 'notify' - it's that
easy.

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
%doc Changes MANIFEST META.yml README scripts/
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/*

%changelog
* Wed Oct 28 2009 Steve Huff <shuff@vecna.org> - 0.99-1
- Initial package.
