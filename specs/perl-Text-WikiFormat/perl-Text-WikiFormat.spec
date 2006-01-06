# $Id$
# Authority: dries
# Upstream: chromatic <chromatic$wgz,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-WikiFormat

Summary: Covert text in a simple Wiki markut language to other tag languages
Name: perl-Text-WikiFormat
Version: 0.77
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-WikiFormat/

Source: http://search.cpan.org/CPAN/authors/id/C/CH/CHROMATIC/Text-WikiFormat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Text::WikiFormat converts text in a simple Wiki markup language to whatever
your little heart desires, provided you can describe it accurately in a
semi-regular tag language.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/WikiFormat.pm
%{perl_vendorlib}/Text/WikiFormat/

%changelog
* Sat Dec 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.77-1
- Initial package.
