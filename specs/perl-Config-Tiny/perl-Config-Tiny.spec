# $Id$

# Authority: dries
# Upstream: Adam Kennedy <cpan$al,as>

%define real_name Config-Tiny
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Read and write ini style files
Name: perl-Config-Tiny
Version: 2.00
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-Tiny/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Config-Tiny-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Config::Tiny is a perl class to read and write .ini style configuration
files with as little code as possible, reducing load time and memory
overhead. Memory usage is normally scoffed at in Perl, but in my opinion
should be at least kept in mind.

This module is primarily for reading human written files, and anything
we write shouldn't need to have documentation/comments. If you need
something with more power, move up to Config::Simple, Config::General or
one of the many other Config:: modules. To rephrase, Config::Tiny does
not preserve your comments, whitespace, or the order of your config
file.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes LICENSE
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Config/Tiny.pm

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.00-1
- Initial package.
