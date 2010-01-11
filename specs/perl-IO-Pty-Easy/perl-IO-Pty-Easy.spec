# $Id$
# Authority: shuff
# Upstream: Jesse Luehrs <doy$tozt,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Pty-Easy

Summary: Easy interface to IO::Pty
Name: perl-%{real_name}
Version: 0.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Pty-Easy/

Source: http://search.cpan.org/CPAN/authors/id/D/DO/DOY/IO-Pty-Easy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::Pty)
BuildRequires: perl(Scalar::Util)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(IO::Pty)
Requires: perl(Scalar::Util)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
IO::Pty::Easy provides an interface to IO::Pty which hides most of the ugly
details of handling ptys, wrapping them instead in simple spawn/read/write
commands.

IO::Pty::Easy uses IO::Pty internally, so it inherits all of the portability
restrictions from that module.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/IO/Pty/
%{perl_vendorlib}/IO/Pty/*

%changelog
* Mon Jan 11 2010 Steve Huff <shuff@vecna.org> - 0.08-1
- Initial package.
