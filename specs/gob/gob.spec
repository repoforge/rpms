# $Id$

# Authority: dag

# Soapbox: 0

Summary: GOB, The GTK+ Object Builder.
Name: gob
Version: 1.0.12
Release: 0
License: GPL
Group: Development/Tools
URL: http://www.5z.com/jirka/gob.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.5z.com/pub/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
GOB is a simple preprocessor for making GTK+ objects.  It makes objects from a
single file which has inline C code so that you don't have to edit the
generated files.  Syntax is somewhat inspired by java and yacc.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README TODO
%doc -P examples/[^M]*
%doc %{_mandir}/man1/*
%{_bindir}/*
%{_datadir}/aclocal/*

%changelog
* Tue Jan 07 2003 Dag Wieers <dag@wieers.com> - 1.0.12
- Initial package. (using DAR)
