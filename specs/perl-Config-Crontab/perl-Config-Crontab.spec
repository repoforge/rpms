# $Id$
# Authority: dries
# Upstream: Scott Wiersdorf <scott$mailblock,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-Crontab

Summary: Read and write Vixie compatible crontab files
Name: perl-Config-Crontab
Version: 1.20
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-Crontab/

Source: http://search.cpan.org/CPAN/authors/id/S/SC/SCOTTW/Config-Crontab-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Config::Crontab reads and writes (and pretty-prints) your crontab(5)
files. It is compatible with Vixie-style crontabs (and all subsets,
including Solaris' SysV-style crontabs).

Config::Crontab has a simple, object-oriented syntax. Crontab files
are broken into "blocks" (paragraphs, each separated by two or more
newlines); the Block is the basic unit of a Config::Crontab object.

You can re-order entire blocks within a crontab file, re-order lines
within blocks (there are three types of lines: comments, environment
settings, and crontab commands or events), remove blocks or lines
within blocks, add new blocks or lines within blocks, etc. See the
Config::Crontab manpage for full details.

Config::Crontab will do basic regular expression syntax checks; it
won't allow obvious garbage (e.g., 'F * * * * /bin/bar' would fail
since 'F' is not valid), but it won't check for nonsensical entries
such as '10-2 * * * * /bin/bar' (the minute range specified is
invalid). However, if you attempt to commit an invalid crontab, the
'write' method will return undef and the 'error' method will be set
(with the output of crontab(1)) if the crontab is rejected by the
crontab program.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Config/Crontab.pm

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.11-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Updated to release 1.11.

* Sat Dec 10 2005 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Initial package.
