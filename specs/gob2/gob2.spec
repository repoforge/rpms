# Authority: dag

# Soapbox: 0

Summary: The GTK+ Object Builder, a preprocessor for making GObjects with inline C code.
Name: gob2
Version: 2.0.5
Release: 0
License: GPL
Group: Development/Tools
URL: http://www.5z.com/jirka/gob.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.5z.com/pub/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: glib2-devel >= 2.0.0

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
* Tue Jan 07 2003 Dag Wieers <dag@wieers.com> - 2.0.5
- Initial package. (using DAR)
