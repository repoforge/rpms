# $Id$
# Authority: shuff
# Upstream: Adam Kennedy <adamk$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-LocalizeNewlines

Summary: Localize the newlines for one or more files
Name: perl-File-LocalizeNewlines
Version: 1.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-LocalizeNewlines/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/File-LocalizeNewlines-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.5
BuildRequires: perl(Class::Default) >= 1.0
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Find::Rule) >= 0.20
BuildRequires: perl(File::Remove) >= 1.42
BuildRequires: perl(File::Slurp) >= 9999.04
BuildRequires: perl(File::Spec) >= 0.80
BuildRequires: perl(FileHandle)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Params::Util) >= 0.10
BuildRequires: perl(Test::More) >= 0.42
BuildRequires: perl(Test::Script) >= 1.02
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.5
Requires: perl(Class::Default) >= 1.0
Requires: perl(File::Find::Rule) >= 0.20
Requires: perl(File::Slurp) >= 9999.04
Requires: perl(File::Spec) >= 0.80
Requires: perl(FileHandle)
Requires: perl(Getopt::Long)
Requires: perl(Params::Util) >= 0.10

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
For people that routinely work with a mixture of different platforms that have
conflicting newline formats (mainly *NIX and Win32) there are a number of
different situations that can result in files having their newlines get
corrupted.

File::LocalizeNewlines provides a mechanism for one off or bulk detection and
conversion of these files to the newline style for the local platform.

The module implements the conversion using a standard "universal line
seperator" regex, which ensures that files with any of the different newlines,
plus a couple of common "broken" newlines, including multiple different types
mixed in the same file, are all converted to the local platform's newline
style.

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
#%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE META.yml README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{perl_vendorlib}/File/LocalizeNewlines.pm
#%{perl_vendorlib}/File/LocalizeNewlines/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Wed Jun 15 2011 Steve Huff <shuff@vecna.org> - 1.12-1
- Initial package.
