# $Id$

# Authority: dries
# Upstream: Mark Jason Dominus (e*Pae**ae?(R)) (=Mark Jason Dominus) <mjd$plover,com>


%define real_name Devel-Trace
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Trace perl programs
Name: perl-Devel-Trace
Version: 0.10
Release: 1
License: Unknown
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-Trace/

Source: http://search.cpan.org/CPAN/authors/id/M/MJ/MJD/Devel-Trace-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
If you run your program with "perl -d:Trace program", this module will
print a message to standard error just before each line is executed, like
the "-x" option of bash.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/Devel/Trace/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Devel/Trace.pm

%changelog
* Sat Jun 12 2004 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Initial package.
