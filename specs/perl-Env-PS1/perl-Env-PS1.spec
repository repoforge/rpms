# $Id$
# Authority: shuff
# Upstream: Jaap Karssenberg <pardus$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Env-PS1

Summary: Prompt string formatter
Name: perl-%{real_name}
Version: 0.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Env-PS1/

Source: http://search.cpan.org/CPAN/authors/id/R/RS/RSN/Env-PS1-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(AutoLoader)
BuildRequires: perl(AutoSplit)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(POSIX)
BuildRequires: perl(Sys::Hostname)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(AutoLoader)
Requires: perl(POSIX)
Requires: perl(Sys::Hostname)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This package supplies variables that are "tied" to environment variables like
PS1 and PS2, if read it takes the contents of the variable as a format string
like the ones bash uses to format the prompt.

It is intended to be used in combination with the various ReadLine packages.

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
%doc Changes MANIFEST README example.pl
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Env/
%{perl_vendorlib}/Env/*
%{perl_vendorlib}/auto/Env/*

%changelog
* Fri Mar 12 2010 Steve Huff <shuff@vecna.org> - 0.06-1
- Initial package.
