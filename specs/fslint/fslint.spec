# $Id$

# Authority: dag

# Soapbox: 0
# Dists: rhfc1 rhel3 rh90 rh80

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

%define real_name FSlint

Summary: utility to find and clean "lint" on a filesystem
Name: fslint
Version: 2.04
Release: 0
License: GPL
Group: System Environment/Base
URL: http://www.pixelbeat.org/fslint/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.iol.ie/~padraiga/fslint/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
BuildRequires: pygtk2-devel
Requires: python >= 2.0, pygtk2, pygtk2-libglade, textutils >= 2.0.21, gettext >= 0.11.1, cpio

%description
FSlint is a utility to find and clean "lint" on a filesystem.
It is written in Python, using pyGtk and libGlade.

%prep
%setup -n %{real_name}-%{version}

%{__perl} -pi.orig -e 's|^liblocation=.*$|liblocation="%{_datadir}/fslint"|' FSlint

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_datadir}/pixmaps/ \
			%{buildroot}%{_datadir}/fslint/fslint/{fstool,rmlint}
%{__install} -m0755 FSlint %{buildroot}%{_bindir}/fslint
%{__ln_s} -f %{_bindir}/fslint %{_bindir}/FSlint
%{__install} -m0755 FSlint %{buildroot}%{_bindir}
%{__install} -m0644 fslint_icon.png %{buildroot}%{_datadir}/pixmaps/
%{__install} -m0644 fslint_icon.png %{buildroot}%{_datadir}/fslint/
%{__install} -m0644 fslint.glade %{buildroot}%{_datadir}/fslint/
%{__install} -m0755 fslint/{find*,fsl*,get*,zipdir} %{buildroot}%{_datadir}/fslint/fslint/
%{__install} -m0755 fslint/fstool/* %{buildroot}%{_datadir}/fslint/fslint/fstool/
%{__install} -m0755 fslint/rmlint/* %{buildroot}%{_datadir}/fslint/fslint/rmlint/

%makeinstall -C po \
	DATADIR="%{buildroot}%{_datadir}"
%find_lang %{name}

%if %{dfi}
        %{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Applications/
        %{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Applications/
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications
        desktop-file-install --vendor gnome                \
                --add-category X-Red-Hat-Base              \
                --add-category Application                 \
                --add-category Utility                     \
                --dir %{buildroot}%{_datadir}/applications \
                %{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc doc/*
%{_bindir}/*
%{_datadir}/fslint/
%{_datadir}/pixmaps/*
%if %{dfi}
        %{_datadir}/gnome/apps/Applications/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 2.04-0
- Updated to release 2.04.

* Wed Jul 30 2003 Dag Wieers <dag@wieers.com> - 2.02-0
- Updated to release 2.02.
- Initial package. (using DAR)
