%define name 	makepasswd
%define version 0.4.2
%define release %mkrel 4

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Generate random passwords
Source0: 	http://www.defora.org/projects/makepasswd/files/%{name}-%{version}.tar.bz2
License: 	GPL
Group: 		System/Configuration/Other
URL: 		http://www.defora.org/index.php?page=projects&project=makepasswd
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
Makepasswd generates pseudo-random passwords of a desired length. It is able
to generate its crypted equivalent.

%prep
%setup -q

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -fr %{buildroot}
%makeinstall PREFIX=%{buildroot}/%{_prefix}
chmod 644 AUTHORS BUGS README

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS BUGS README
%{_bindir}/makepasswd

