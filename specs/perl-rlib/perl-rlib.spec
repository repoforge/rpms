# $Id$
# Authority: dfateyev
# Upstream: Graham Barr <gbarr$pobox,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name rlib

%define perl_prefix %{buildroot}%{_prefix}

Summary: manipulate @INC at compile time with relative paths
Name: perl-%{real_name}
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/%{real_name}/

Source: %{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: rpm-macros-rpmforge

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{perl_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/%{real_name}.pm


%changelog
* Mon May 28 2011 Rocky Bernstein <rocky@cpan.org> - 0.02-1
- Initial package.
