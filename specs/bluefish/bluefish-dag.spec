# Authority: freshrpms

Summary: A GTK2 web development application for experienced users.
Name: bluefish
Version: 0.9
Release: 0
Group: Development/Tools
License: GPL
URL: http://bluefish.openoffice.nl/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://bluefish.openoffice.nl/download/%{name}-%{version}.tar.bz2
Patch: bluefish-0.9-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gtk2-devel >= 2.0.6, pcre-devel >= 3.9

%description
Bluefish is a GTK+ HTML editor for the experienced web designer or
programmer. It is not finished yet, but already a very powerful site
creating environment. Bluefish has extended support for programming
dynamic and interactive websites, there is for example a lot of PHP
support.

%prep
%setup
%patch -p1 -b .makefile

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_datadir}/pixmaps \
			%{buildroot}%{_datadir}/applications
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

desktop-file-install --vendor "gnome" --delete-original \
  --add-category X-Red-Hat-Base                         \
  --add-category Application                            \
  --add-category Development                            \
  --dir %{buildroot}%{_datadir}/applications            \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYING PORTING
%{_bindir}/*
%{_datadir}/bluefish/
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Tue Feb 25 2003 Dag Wieers <dag@wieers.com> - 0.9-0
- Initial package. (using DAR)
