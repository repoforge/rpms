# $Id: perl-IP-Country.spec 201 2004-04-03 15:24:49Z dag $
# Authority: dag
# Upstream: Andrew Arensburger <arensb$ooblick,com>

%define perl_vendorlib  %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch  %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name p5-Palm
%define real_version 1.003_000

Summary: Perl Palm classes
Name: perl-Palm
Version: 1.3.0
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/p5-Palm/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/A/AR/ARENSB/p5-Palm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Perl Palm classes.

%prep
%setup -n %{real_name}-%{real_version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc FAQ MANIFEST README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{perl_vendorlib}/*

%changelog
* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 1.3.0-1
- Initial package. (using DAR)
