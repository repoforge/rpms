# $Id$
# Authority: dag
# Upstream: Andrew Arensburger <arensb$ooblick,com>

%define perl_vendorlib  %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch  %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name p5-Palm
%define real_version 1.003_000

Summary: Perl Palm classes
Name: perl-Palm
Version: 1.3.0
Release: 2.2
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/p5-Palm/

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
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.0-2.2
- Rebuild for Fedora Core 5.

* Sat Oct 15 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.0-2
- Fixed the source url.

* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 1.3.0-1
- Initial package. (using DAR)
