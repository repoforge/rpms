# Authority: dag

Summary: A GNOME UML modeling environment.
Name: gaphor
Version: 0.2.0
Release: 0
Group: Development/Tools
License: GPL
URL: http://gaphor.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/gaphor/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
Gaphor is a new project. The goal is to create an easy to use modeling
environment. This means that you are able to create nice UML diagrams
for documentation and to assist you with design decisions. Gaphor will
help you create your applications.

%prep
%setup

%build
%configure

%install
%{__rm} -rf %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS NEWS PKG-INFO README TODO doc/*.txt
%{_bindir}/*
%{_datadir}/pixmaps/gv4l/gv4l.png
%{_datadir}/applications/*

%changelog
* Mon Apr 07 2003 Dag Wieers <dag@wieers.com> - 0.2.0-0
- Initial package. (using DAR)
